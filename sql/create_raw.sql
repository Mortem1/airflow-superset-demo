CREATE SCHEMA IF NOT EXISTS airflow_data;
CREATE TABLE IF NOT EXISTS airflow_data.sales_raw (
    id SERIAL PRIMARY KEY,
    sale_date DATE,
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price NUMERIC(10,2)
);

TRUNCATE TABLE airflow_data.sales_raw RESTART IDENTITY;

INSERT INTO airflow_data.sales_raw (sale_date, product, category, quantity, price)
SELECT
    CURRENT_DATE - (random() * 30)::int AS sale_date,
    (ARRAY['Ноутбук', 'Мышь', 'Клавиатура', 'Монитор', 'Принтер'])[floor(random() * 5 + 1)] AS product,
    (ARRAY['Электроника', 'Аксессуары', 'Офис'])[floor(random() * 3 + 1)] AS category,
    floor(random() * 10 + 1)::int AS quantity,
    round((random() * 100 + 10)::numeric, 2) AS price
FROM generate_series(1, 30);