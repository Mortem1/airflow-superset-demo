from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/opt/airflow/python')
from process_sales import process_sales_data

def read_sql_file(path):
    with open(path, 'r') as f:
        return f.read()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='sales_pipeline_organized',
    default_args=default_args,
    schedule=None,
    catchup=False,
) as dag:

    create_raw = SQLExecuteQueryOperator(
        task_id='create_raw',
        conn_id='postgres',
        sql=read_sql_file('/opt/airflow/sql/create_raw.sql')
    )

    process = PythonOperator(
        task_id='process_sales',
        python_callable=process_sales_data,
    )

    aggregate = SQLExecuteQueryOperator(
        task_id='aggregate',
        conn_id='postgres',
        sql=read_sql_file('/opt/airflow/sql/create_aggregated.sql')
    )

    create_raw >> process >> aggregate