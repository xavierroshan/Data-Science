import functions_framework
import pymongo
import mysql.connector
import json
from datetime import datetime, timedelta
import logging
from google.cloud import storage
import os
from google.auth import jwt
from http import HTTPStatus

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MySQL Cloud SQL connection details (use environment variables)
MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST', '127.0.0.1'),  # Cloud SQL Auth Proxy
    'user': os.getenv('MYSQL_USER', 'app_user'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE', 'crm_db')
}

# MongoDB connection details
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://username:password@localhost:27017/automobile_db')
MONGO_DB_NAME = 'automobile_db'
COMPONENT_CONFIGS_COLLECTION = 'component_configs'

# Google Cloud Storage bucket
GCS_BUCKET = os.getenv('GCS_BUCKET', 'your-bucket-name')

# Expected service account for Cloud Scheduler OIDC authentication
EXPECTED_AUDIENCE = os.getenv('EXPECTED_AUDIENCE', f'https://us-central1-YOUR_PROJECT_ID.cloudfunctions.net/generate_master_config')

def validate_request(request):
    """Validate the HTTP request method and authentication."""
    # Check if the request method is POST
    if request.method != 'POST':
        logger.error(f"Invalid request method: {request.method}")
        return {"status": "error", "message": f"Method {request.method} not allowed, use POST"}, HTTPStatus.METHOD_NOT_ALLOWED

    # Validate OIDC token from Cloud Scheduler
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        logger.error("Missing or invalid Authorization header")
        return {"status": "error", "message": "Unauthorized: Missing or invalid token"}, HTTPStatus.UNAUTHORIZED

    try:
        token = auth_header.split('Bearer ')[1]
        # Verify the JWT token
        decoded_token = jwt.decode(token, verify=False)  # Note: In production, verify with Google's public keys
        if decoded_token.get('aud') != EXPECTED_AUDIENCE:
            logger.error(f"Invalid audience in token: {decoded_token.get('aud')}")
            return {"status": "error", "message": "Unauthorized: Invalid token audience"}, HTTPStatus.UNAUTHORIZED
        logger.info(f"Request authenticated for issuer: {decoded_token.get('iss')}")
    except Exception as e:
        logger.error(f"Token validation failed: {e}")
        return {"status": "error", "message": f"Unauthorized: Token validation failed - {str(e)}"}, HTTPStatus.UNAUTHORIZED

    return None

def connect_to_mysql():
    """Connect to MySQL Cloud SQL and return the connection object."""
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        logger.info("Connected to MySQL Cloud SQL")
        return conn
    except mysql.connector.Error as e:
        logger.error(f"Failed to connect to MySQL: {e}")
        raise

def connect_to_mongodb():
    """Connect to MongoDB and return the database object."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        logger.info("Connected to MongoDB")
        return db
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise

def get_daily_orders(mysql_conn):
    """Retrieve customer orders for the current day from MySQL."""
    try:
        cursor = mysql_conn.cursor(dictionary=True)
        today = datetime.now().strftime('%Y-%m-%d 00:00:00')
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        query = """
            SELECT order_id, customer_id, components, order_date
            FROM customer_orders
            WHERE order_date >= %s AND order_date < %s
        """
        cursor.execute(query, (today, tomorrow))
        orders = cursor.fetchall()
        cursor.close()
        logger.info(f"Found {len(orders)} orders for processing")
        return orders
    except mysql.connector.Error as e:
        logger.error(f"Error fetching daily orders from MySQL: {e}")
        raise

def get_component_config(db, component_id):
    """Fetch configuration for a specific component from MongoDB."""
    try:
        config = db[COMPONENT_CONFIGS_COLLECTION].find_one({"component_id": component_id})
        if not config:
            logger.warning(f"No config found for component: {component_id}")
        return config
    except Exception as e:
        logger.error(f"Error fetching config for component {component_id}: {e}")
        raise

def generate_master_config(order, component_configs):
    """Generate master configuration by combining component configs."""
    try:
        if not component_configs or any(c is None for c in component_configs):
            return None
        master_config = {
            "order_id": order["order_id"],
            "customer_id": order["customer_id"],
            "components": {},
            "generated_at": datetime.now().isoformat()
        }
        for component_id, config in component_configs:
            master_config["components"][component_id] = config.get("config", {})
        return master_config
    except Exception as e:
        logger.error(f"Error generating master config for order {order['order_id']}: {e}")
        raise

def save_config_to_gcs(config, order_id):
    """Save the master configuration to a Google Cloud Storage bucket."""
    try:
        if not config:
            return
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(GCS_BUCKET)
        blob = bucket.blob(f"configs/master_config_{order_id}.json")
        blob.upload_from_string(json.dumps(config, indent=2))
        logger.info(f"Uploaded master config for order {order_id} to gs://{GCS_BUCKET}/configs/master_config_{order_id}.json")
    except Exception as e:
        logger.error(f"Error uploading master config for order {order_id}: {e}")
        raise

@functions_framework.http
def generate_master_config(request):
    """Cloud Function entry point triggered by HTTP request."""
    # Validate the request
    validation_error = validate_request(request)
    if validation_error:
        return validation_error

    # Log request headers for debugging
    logger.info(f"Request headers: {dict(request.headers)}")
    
    # Check for optional JSON payload
    try:
        request_json = request.get_json(silent=True)
        if request_json:
            logger.info(f"Request payload: {request_json}")
    except Exception as e:
        logger.warning(f"Failed to parse request payload: {e}")
        return {"status": "error", "message": "Invalid JSON payload"}, HTTPStatus.BAD_REQUEST

    try:
        # Connect to databases
        mysql_conn = connect_to_mysql()
        mongo_db = connect_to_mongodb()
        
        # Get daily orders from MySQL
        orders = get_daily_orders(mysql_conn)
        
        # Process each order
        for order in orders:
            order_id = order["order_id"]
            components = json.loads(order["components"]) if isinstance(order["components"], str) else order["components"]
            
            # Fetch configurations for each component
            component_configs = []
            for component_id in components:
                config = get_component_config(mongo_db, component_id)
                if config:
                    component_configs.append((component_id, config))
                else:
                    logger.warning(f"Skipping component {component_id} for order {order_id}: No config found")
            
            # Generate master config
            master_config = generate_master_config(order, component_configs)
            if not master_config:
                logger.warning(f"Skipping order {order_id}: Failed to generate master config")
                continue
            
            # Save to GCS
            save_config_to_gcs(master_config, order_id)
        
        logger.info("Master configuration generation completed successfully")
        return {"status": "success", "message": f"Processed {len(orders)} orders"}, HTTPStatus.OK
    except Exception as e:
        logger.error(f"Function failed: {e}")
        return {"status": "error", "message": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        if 'mysql_conn' in locals() and mysql_conn.is_connected():
            mysql_conn.close()
            logger.info("Closed MySQL connection")