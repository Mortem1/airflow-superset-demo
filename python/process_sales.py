import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

def process_sales_data():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    df = pg_hook.get_pandas_df("SELECT * FROM airflow_data.sales_raw;")

    df['total'] = df['quantity'] * df['price']
    df['month'] = pd.to_datetime(df['sale_date']).dt.month
    df['weekday'] = pd.to_datetime(df['sale_date']).dt.day_name()

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS airflow_data.sales_processed (
        id INT,
        sale_date DATE,
        product VARCHAR(100),
        category VARCHAR(50),
        quantity INT,
        price NUMERIC(10,2),
        total NUMERIC(10,2),
        month INT,
        weekday VARCHAR(20)
    );
    """
    pg_hook.run(create_table_sql)
    pg_hook.run("TRUNCATE TABLE airflow_data.sales_processed;")

    rows = df[['id', 'sale_date', 'product', 'category', 'quantity', 'price', 'total', 'month', 'weekday']].values.tolist()
    pg_hook.insert_rows(
        table='airflow_data.sales_processed',
        rows=rows,
        target_fields=['id', 'sale_date', 'product', 'category', 'quantity', 'price', 'total', 'month', 'weekday']
    )