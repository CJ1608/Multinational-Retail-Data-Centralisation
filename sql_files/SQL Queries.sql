-- Find how many stores each business have in each country
UPDATE dim_store_details
SET "country_code" = 'N/A'
WHERE index=0;

UPDATE dim_store_details
SET "continent" = 'N/A'
WHERE index=0;

SELECT country_code, COUNT(*)
FROM dim_store_details
GROUP BY country_code

	
-- Find locations that have the most stores
SELECT locality, COUNT(*)
FROM dim_store_details
GROUP BY locality
ORDER BY count DESC
LIMIT 7

	
-- Find which months produced the largest number of sales
SELECT dim_date_times.month, ROUND(CAST(SUM(orders_table.product_quantity*dim_products.product_price) AS NUMERIC), 2) AS profit
FROM dim_date_times
INNER JOIN orders_table 
	ON dim_date_times.date_uuid = orders_table.date_uuid
INNER JOIN dim_products
	ON orders_table.product_code = dim_products.product_code
GROUP BY dim_date_times.month
ORDER BY profit DESC


-- Find how many sales are from online 
SELECT COUNT(orders_table.product_code) AS num_sales, SUM(orders_table.product_quantity) AS prod_count, --dim_store_details.store_type,
CASE
	WHEN dim_store_details.store_type ='Web Portal' THEN 'Web'
	WHEN dim_store_details.store_type != 'Web Store' THEN 'Offline'
	END location
FROM orders_table
INNER JOIN dim_store_details
	ON orders_table.store_code = dim_store_details.store_code
GROUP BY location


-- Find what % of sales come through each store type
SELECT dim_store_details.store_type, 
	ROUND(CAST(SUM(orders_table.product_quantity * dim_products.product_price) AS numeric), 2) AS total_sales,
	round(SUM(100 * orders_table.product_quantity*dim_products.product_price)/(SUM(SUM(orders_table.product_quantity*dim_products.product_price)) OVER ())) as percentage_total
FROM orders_table
INNER JOIN dim_store_details
	ON orders_table.store_code = dim_store_details.store_code
INNER JOIN dim_products
	ON orders_table.product_code = dim_products.product_code
GROUP BY dim_store_details.store_type
ORDER BY percentage_total DESC


-- Find which month in every year produced the highest cost of sales
SELECT ROUND(CAST(SUM(orders_table.product_quantity * dim_products.product_price) AS numeric), 2) as total_sales, dim_date_times.year, dim_date_times.month
FROM orders_table
INNER JOIN dim_date_times
	ON orders_table.date_uuid = dim_date_times.date_uuid
INNER JOIN dim_products
	ON orders_table.product_code = dim_products.product_code
GROUP BY dim_date_times.year, dim_date_times.month
order by SUM(orders_table.product_quantity * dim_products.product_price) DESC
LIMIT 10


-- Find the total staff headcount by country code
ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE bigint
USING staff_numbers::bigint

SELECT sum(dim_store_details.staff_numbers) as total_staff_numbers,
CASE
	WHEN dim_store_details.country_code = 'N/A' THEN 'GB'
	WHEN dim_store_details.country_code = 'GB' THEN 'GB'
	WHEN dim_store_details.country_code = 'DE' THEN 'DE'
	WHEN dim_store_details.country_code = 'US' THEN 'US'
	END code
FROM dim_store_details
GROUP BY code
ORDER BY total_staff_numbers desc


-- Find which German store type is selling the most
SELECT dim_store_details.store_type, dim_store_details.country_code, ROUND(CAST(SUM(orders_table.product_quantity * dim_products.product_price) AS numeric), 2) as total_sales
FROM dim_store_details
INNER JOIN orders_table
	ON dim_store_details.store_code = orders_table.store_code
INNER JOIN dim_products
	ON orders_table.product_code = dim_products.product_code
WHERE dim_store_details.country_code='DE'
GROUP BY dim_store_details.store_type, dim_store_details.country_code
ORDER BY total_sales


-- Find how quickly the company is making sales
WITH cte_timestamps AS
(
	SELECT year, TO_TIMESTAMP(CONCAT(dim_date_times.year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD H:M:S') as dt_timestamps
	FROM dim_date_times
	ORDER BY dt_timestamps DESC
), 
cte_compare_timestamps AS
(
	SELECT year, dt_timestamps,
	LEAD(dt_timestamps, 1) OVER (ORDER BY dt_timestamps DESC) as time_difference
	FROM cte_timestamps
)
SELECT year, AVG(dt_timestamps-time_difference) as time_taken 
FROM cte_compare_timestamps
GROUP BY year
ORDER BY time_taken DESC
