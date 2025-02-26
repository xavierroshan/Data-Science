from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, timedelta
import random

default_args = {
    "owner":"airflow",
    "start_date": datetime(2025,2,26),
    "retries": 2,
    "retry_delay":timedelta(minutes=5)

}

def ingest_data():
    print("Ingested the data")

def process_data():
    print("Processed the data")

def validate_data():
    print("Validated the data")

def do_quality_check():
    print ("checked the quality")

def skip_quality_check():
    print("Skipped the quality check")

def clean_up():
    print("Did the cleanup task")

def generate_report():
    print("generated report")

def complete_task():
    print("completed the workflow tasks")

    
def define_branching_policy(**kwargs):
    num = random.randint(10, 20)
    if num % 2 == 0:
        return 'do_quality_check'  # Corrected to return task ID
    else:
        return 'skip_quality_check'  # Corrected to return task ID
    
with DAG(
    'data_processing_pipeline_with_branching',
    default_args= default_args,
    description="simple workflow to test branching",
    schedule="@daily",
    catchup=False

) as dag:
    
    ingest_data_task = PythonOperator(
        task_id = "ingest_data",
        python_callable=ingest_data
    )

    process_data_task = PythonOperator(
        task_id = "process_data",
        python_callable= process_data

    )

    validate_data_task = PythonOperator(
        task_id = "validate_data",
        python_callable=validate_data
    )

    do_quality_check_data_task = PythonOperator(
        task_id = "do_quality_check",
        python_callable=do_quality_check
    )

    skip_quality_check_task = PythonOperator(
        task_id = "skip_quality_check",
        python_callable=skip_quality_check
    )

    clean_up_task = PythonOperator(
        task_id = "clean_up",
        python_callable=clean_up
    )

    generate_report_task = PythonOperator(
        task_id = "generate_report",
        python_callable=generate_report
    )

    complete_task_task = PythonOperator(
        task_id = "complete_task",
        python_callable=complete_task
    )

    define_branching_policy_task = BranchPythonOperator(
        task_id = "define_branching_policy",
        python_callable=define_branching_policy,
    )

    ingest_data_task >> process_data_task >> validate_data_task >> define_branching_policy_task
    define_branching_policy_task >> do_quality_check_data_task
    define_branching_policy_task >> skip_quality_check_task
    do_quality_check_data_task >> [clean_up_task,generate_report_task]
    [clean_up_task,generate_report_task] >> complete_task_task




