DROP TABLE IF EXISTS airflow_data.sales_dashboard;
CREATE TABLE airflow_data.sales_dashboard AS
SELECT
    category,
    DATE_TRUNC('month', sale_date) AS month_start,
    SUM(total) AS total_revenue,
    AVG(total) AS avg_revenue_per_sale,
    COUNT(*) AS num_transactions
FROM airflow_data.sales_processed
GROUP BY category, DATE_TRUNC('month', sale_date)
ORDER BY category, month_start;