from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta


default_args = {
    "owner":"airflow",
    "start_date": datetime(2024,12,25),
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

with DAG (
    dag_id = "mydag1",
    default_args= default_args,
    schedule_interval="@daily",
    catchup=False

) as dag:
    
    start_task = PythonOperator(
        task_id = "start_task",
        python_callable= lambda:print("first task is getting executed")

    )

    process_task = PythonOperator(
        task_id = "process_task",
        python_callable= lambda:print("processing the task")
    )

    final_task = PythonOperator(
        task_id = "final_task",
        python_callable= lambda:print("processing the task")

    )

    start_task >> process_task >> final_task