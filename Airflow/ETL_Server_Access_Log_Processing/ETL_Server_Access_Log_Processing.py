from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


#DAG Arguments
default_args:{
        'owner':'Prathamesh',
        'start_date':days_ago(0),
        'email':['prathamesh@somemail.com'],
        'email_on_failure':'False',
        'email_on_retry':'False',
        'retries':1,
        'retry_delay':timedelta(minutes=5),
        }

#DAG Definition
dag=DAG(
        dag_id='etl_server_access_log_processing',
        default_args=default_args,
        description='etl_server_access_log_processing',
        scheduled_interval=timedelta(days=1)
        )


#Task Definition

download=BashOperator(
        task_id='download',
        bash_command="wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'",
        dag=dag,
        )

extract=BashOperator(
        task_id='extract',
        bash_command='cut -f1,4 -d"#" web-server-access-log.txt > extracted.txt',
        dag=dag,
        )


transform=BashOperator(
        task_id='transform',
        bash_command="tr [:lower:] [:upper:] < extracted.txt > transformed.txt",
        dag=dag,
        )

load=BashOperator(
        task_id='load',
        bash_command="zip log.zip transformed.txt",
        dag=dag,
        )

# Task Pipeline
download >> extract >> transform >> load




