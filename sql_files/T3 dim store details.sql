SELECT * FROM dim_store_details

--long and lat
-- ALTER TABLE dim_store_details
-- ALTER COLUMN longitude TYPE float
-- USING longitude::float

-- ALTER TABLE dim_store_details
-- ALTER COLUMN latitude TYPE float
-- USING latitude::float

-- ALTER TABLE dim_store_details
-- ALTER COLUMN locality TYPE VARCHAR(225)

--ERRORS: M3, T2, STORE CODE NUMBERS?
-- ALTER TABLE dim_store_details
-- ALTER COLUMN store_code TYPE VARCHAR(12)

-- ERROR: M3, T3, STAFF NUMBERS
-- ALTER TABLE dim_store_details
-- ALTER COLUMN staff_numbers TYPE smallint
-- USING staff_numbers::smallint

-- ALTER TABLE dim_store_details
-- ALTER COLUMN opening_date TYPE date

-- ALTER TABLE dim_store_details
-- ALTER COLUMN store_type TYPE VARCHAR(225) 
-- --nullable by default?

-- ALTER TABLE dim_store_details
-- ALTER COLUMN country_code TYPE VARCHAR(2)

-- ALTER TABLE dim_store_details
-- ALTER COLUMN continent TYPE VARCHAR(225)

--REPLACE NULL VALUE IN INDEX 0 WITH 'N/A' FOR ROW 'LATITUDE'
-- UPDATE dim_store_details
-- SET latitude = 'N/A'
-- WHERE latitude IS null

