-- Cast columns to correct data type

SELECT MAX(LENGTH(dim_card_details.card_number))
FROM dim_card_details --returns 19
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19)

SELECT MAX(LENGTH(dim_card_details.expiry_date))
FROM dim_card_details --returns 5
ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE VARCHAR(5)

ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE date

SELECT max(length(orders_table.store_code)) AS longest_store_code
FROM orders_table --gives 12
