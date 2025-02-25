import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of files and records per file
num_files = 10
records_per_file = 500

# Function to generate fake supply chain data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        order_id = fake.uuid4()
        product_id = f"PROD{random.randint(1000, 9999)}"
        product_name = random.choice(["Laptop", "Smartphone", "Tablet", "Headphones", "Monitor"])
        category = random.choice(["Electronics", "Appliances", "Furniture", "Clothing"])
        supplier_id = f"SUPP{random.randint(100, 999)}"
        supplier_name = fake.company()
        order_date = fake.date_between(start_date="-2y", end_date="today").toordinal() - 719163  # Convert to Parquet date format
        shipment_date = fake.date_time_between(start_date="-1y", end_date="now").timestamp() * 1_000_000  # Microseconds
        quantity_ordered = random.randint(1, 100)
        unit_price = round(random.uniform(10, 5000), 2)
        total_cost = round(quantity_ordered * unit_price, 2)
        currency = "USD"
        status = random.choice(["Shipped", "Pending", "Cancelled", "Delivered"])
        warehouse_location = fake.city()
        shipment_tracking = fake.uuid4() if random.random() > 0.2 else None  # 80% chance of having a tracking number

        supplier_contact = {
            "contact_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }

        shipment_details = {
            "carrier": random.choice(["FedEx", "UPS", "DHL", "USPS"]),
            "tracking_number": fake.uuid4() if random.random() > 0.2 else None,
            "estimated_arrival": fake.future_date(end_date="+30d").strftime('%s') + "000000",
            "shipment_status": random.choice(["In Transit", "Pending", "Delivered"])
        }

        data.append([
            order_id, product_id, product_name, category, supplier_id, supplier_name,
            order_date, shipment_date, quantity_ordered, unit_price, total_cost, currency, status,
            warehouse_location, shipment_tracking, supplier_contact, shipment_details
        ])

    return data

# Define Parquet schema
schema = pa.schema([
    pa.field("order_id", pa.string()),
    pa.field("product_id", pa.string()),
    pa.field("product_name", pa.string()),
    pa.field("category", pa.string()),
    pa.field("supplier_id", pa.string()),
    pa.field("supplier_name", pa.string()),
    pa.field("order_date", pa.date32()),
    pa.field("shipment_date", pa.timestamp("us")),
    pa.field("quantity_ordered", pa.int32()),
    pa.field("unit_price", pa.float64()),
    pa.field("total_cost", pa.float64()),
    pa.field("currency", pa.string()),
    pa.field("status", pa.string()),
    pa.field("warehouse_location", pa.string()),
    pa.field("shipment_tracking", pa.string()),
    pa.field("supplier_contact", pa.struct([
        pa.field("contact_name", pa.string()),
        pa.field("email", pa.string()),
        pa.field("phone", pa.string())
    ])),
    pa.field("shipment_details", pa.struct([
        pa.field("carrier", pa.string()),
        pa.field("tracking_number", pa.string()),
        pa.field("estimated_arrival", pa.timestamp("us")),
        pa.field("shipment_status", pa.string())
    ]))
])

# Generate and save 10 Parquet files
for i in range(1, num_files + 1):
    file_name = f"supply_chain_data_{i}.parquet"
    
    # Generate random records
    records = generate_data(records_per_file)
    
    # Create a DataFrame
    df = pd.DataFrame(records, columns=schema.names)
    
    # Convert to Arrow Table
    table = pa.Table.from_pandas(df, schema=schema)
    
    # Save as Parquet file
    pq.write_table(table, file_name)
    
    print(f"Generated {file_name} with {records_per_file} records.")

print("Parquet files created successfully!")