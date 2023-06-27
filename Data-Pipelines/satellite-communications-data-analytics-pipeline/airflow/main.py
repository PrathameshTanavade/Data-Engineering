from datetime import timedelta

from datetime import timedelta

from airflow.models import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

import pendulum


default_args = {
    'owner': 'Prathamesh',
    'start_date': pendulum.today('UTC').add(days=0),
    'email': ['prathamesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}




DAG_ID="sat_comm"

with DAG(
        'sat_comm',
        default_args=default_args,
        description='Satellite Communication Airflow DAG',
        schedule=timedelta(hours=1)) as dag:


        submit_job = SparkSubmitOperator(
                application="../pyspark/sat_comm_pyspark.py ",
                task_id="submit_job",
        )


