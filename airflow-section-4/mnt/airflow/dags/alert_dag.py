from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

def on_success_task(dict):
    print("Success")
    print(dict)

def on_failure_task(dict):
    print("Failure")
    print(dict)


default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
    'retries':3,
    'retry_delay':timedelta(seconds=60),
    'on_failure_callback':on_failure_task,
    'on_success_callback':on_success_task,
    'execution_timeout':timedelta(seconds=60),
}

with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=True) as dag:
    
    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="exit 1")
    
    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2