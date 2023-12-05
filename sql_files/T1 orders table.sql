--TASK 1, CAST COLUMNS

-- ALTER TABLE orders_table
-- ALTER COLUMN date_uuid TYPE UUID
-- USING date_uuid::UUID;

-- ALTER TABLE orders_table
-- ALTER COLUMN user_uuid TYPE UUID
-- USING user_uuid::UUID;

-- ALTER TABLE orders_table
-- ALTER COLUMN product_quantity TYPE smallint
-- USING product_quantity::smallint

-- SELECT max(length(orders_table.card_number)) AS lcn
-- FROM orders_table

-- SELECT max(length(orders_table.store_code)) AS longest_store_code
-- FROM orders_table --gives 12
-- ALTER TABLE orders_table 
-- ALTER COLUMN store_code TYPE VARCHAR(13) 
-- USING store_code::VARCHAR(13);

-- SELECT max(length(orders_table.product_code))
-- FROM orders_table -- gives 11
-- ALTER TABLE orders_table
-- ALTER COLUMN product_code TYPE VARCHAR(12)
-- USING product_code::VARCHAR(12)

-- ALTER TABLE orders_table
-- ALTER COLUMN card_number TYPE VARCHAR
-- USING card_number::VARCHAR
-- SELECT max(length(orders_table.card_number))
-- FROM orders_table --returns 19
-- ALTER TABLE orders_table 
-- ALTER COLUMN card_number TYPE VARCHAR(20)
-- USING card_number::VARCHAR(20)

SELECT * FROM orders_table