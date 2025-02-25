from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import random


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def decide_branch(**kwargs):
    return "process_data" if random.choice([True, False]) else "skip_task"


with DAG(
    dag_id="common_methods_example",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:


    start_task = BashOperator(
        task_id="start",
        bash_command="echo 'Starting DAG execution'",
    )

    branch_task = BranchPythonOperator(
        task_id="branch_task",
        python_callable=decide_branch,
        provide_context=True,
    )


    process_task = PythonOperator(
        task_id="process_data",
        python_callable=lambda: print("Processing data..."),
    )


    skip_task = BashOperator(
        task_id="skip_task",
        bash_command="echo 'Skipping process'",
    )


    wait_for_file = FileSensor(
        task_id="wait_for_file",
        filepath="/tmp/input_data.csv",
        poke_interval=10,
    )


    notify_task = BashOperator(
        task_id="notify",
        bash_command="echo 'Pipeline completed successfully'",
    )


    start_task >> branch_task
    branch_task >> [process_task, skip_task]
    process_task >> wait_for_file >> notify_task