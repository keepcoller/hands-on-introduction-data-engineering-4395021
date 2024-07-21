'''One Task Dag'''

from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
        'owner': 'Vinoo',
        'depends_on_past': False,
        'e-mail_on_failure': False,
        'e-mail_on_retry':False,
        'retries': 0,
        'catchup':False,
        'start_date':datetime(2023,1,1)

}

with DAG (
    dag_id='one_task_dag',
    description='A one task Airflow DAG',
    schedule_interval= None,
    default_args=default_args

) as dag:
    
    task1 = BashOperator(
        task_id='one_task',
        bash_command='echo "hello linkedin learning!" > /workspaces/hands-on-introduction-data-engineering-4395021/lab/temp/create_this_file.txt',
        dag =dag

)  