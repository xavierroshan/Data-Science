import datetime
import subprocess
import os

from google.cloud import storage, bigquery

PROJECT = os.environ["GCP_PROJECT"]
BUCKET = "my-cloudsql-bq-export"
INSTANCE = "my-sql-instance"
DB = "crm_db"
TABLE = "customers"
DATASET = "my_dataset"
STAGING_TABLE = f"{DATASET}.customers_staging"
MAIN_TABLE = f"{DATASET}.customers"

def export_csv():
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    file_path = f"gs://{BUCKET}/customers_{date_str}.csv"
    query = f"SELECT * FROM {TABLE} WHERE updated_at > DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)"
    
    subprocess.run([
        "gcloud", "sql", "export", "csv", INSTANCE,
        file_path,
        f"--database={DB}",
        f"--query={query}"
    ], check=True)
    
    return file_path

def load_to_bigquery(uri):
    client = bigquery.Client()
    
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
        write_disposition="WRITE_TRUNCATE"
    )

    load_job = client.load_table_from_uri(
        uri, STAGING_TABLE, job_config=job_config
    )
    load_job.result()

def merge_to_main():
    client = bigquery.Client()
    query = f"""
    MERGE `{MAIN_TABLE}` T
    USING `{STAGING_TABLE}` S
    ON T.customer_id = S.customer_id
    WHEN MATCHED THEN UPDATE SET *
    WHEN NOT MATCHED THEN INSERT ROW
    """
    client.query(query).result()

def main(request):
    file_path = export_csv()
    load_to_bigquery(file_path)
    merge_to_main()
    return "Daily sync completed"
