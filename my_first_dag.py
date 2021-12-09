from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Udit',
    'depends_on_past': False,
    'start_date': datetime(2021,9,1),
    'email': ['udit@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# define the DAG
dag = DAG(
    'my_first_dag',
    default_args=default_args,
    description='Getting Started with Airflow')

task1 = BashOperator(task_id='task1',bash_command='echo "Hello from task1"',dag=dag)

task2 = BashOperator(task_id='task2',bash_command='echo "Hello from task2"',dag=dag)

task1 >> task2


