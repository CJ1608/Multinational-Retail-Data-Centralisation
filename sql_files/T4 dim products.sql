SELECT * from dim_products
ORDER BY index ASC

--remove £ character from product  price column
-- UPDATE dim_products
-- SET product_price = REPLACE(product_price, '£', '')

--add weight class column to table 			
-- ALTER TABLE dim_products
-- ADD COLUMN weight_class VARCHAR;
-- UPDATE dim_products
-- SET weight_class = 'Light'
-- WHERE weight < 2;
-- UPDATE dim_products
-- SET weight_class = 'Mid_Sized'
-- WHERE weight >= 2 and weight < 40;
-- UPDATE dim_products
-- SET weight_class = 'Heavy'
-- WHERE weight >=40 and weight < 140;
-- UPDATE dim_products
-- SET weight_class = 'Truck_Required'
-- WHERE weight >=140;

--change data types 
-- ALTER TABLE dim_products
-- ALTER COLUMN product_price TYPE float
-- USING product_price::float;

-- SELECT max(length(dim_products."EAN"))
-- FROM dim_products  --returns 17
-- ALTER TABLE dim_products
-- ALTER COLUMN "EAN" TYPE varchar(17)

-- SELECT max(length(dim_products."product_code"))
-- FROM dim_products --returns 11
-- ALTER TABLE dim_products
-- ALTER COLUMN product_code TYPE varchar(11)

-- ALTER TABLE dim_products
-- ALTER COLUMN date_added TYPE date

-- ALTER TABLE dim_products
-- ALTER COLUMN "uuid" TYPE UUID
-- USING uuid::UUID

-- ALTER TABLE dim_products
-- ALTER COLUMN availability
-- SET data type boolean 
-- USING CASE
-- 	WHEN "availability" = 'Still_avaliable' then true
-- 	WHEN "availability" = 'Removed' then false
-- END

-- SELECT max(length(dim_products."weight_class"))
-- FROM dim_products --returns 14
-- ALTER TABLE dim_products
-- ALTER COLUMN weight_class TYPE varchar(14)