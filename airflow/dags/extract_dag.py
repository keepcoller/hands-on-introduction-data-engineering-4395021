'''Extract_data_using_dag'''

from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG


#Default settings applied to all tags

with DAG (
        dag_id = 'extract_dag',
        description= 'Dag to show how to extract data',
        schedule_interval=None,
        catchup=False ) as dag:
    
    extract_task = BashOperator (

        task_id='extract_task',
        catchup=False 
        bash_command= 'wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/manual/manual-extract.csv'

    )
         

