
--USER ID PK
ALTER TABLE dim_users
DROP CONSTRAINT user_uuid_pkey
ALTER TABLE dim_users
ADD CONSTRAINT user_uuid_pkey
PRIMARY KEY (user_uuid)

--STORE CODE PK
ALTER TABLE dim_store_details
DROP CONSTRAINT store_code_pkey
ALTER TABLE dim_store_details
ADD CONSTRAINT store_code_pkey
PRIMARY KEY (store_code)

--PRODUCT CODE PK
ALTER TABLE dim_products
DROP CONSTRAINT product_code_pkey
ALTER TABLE dim_products
ADD CONSTRAINT product_code_pkey
PRIMARY KEY (product_code)

--DIM DATE PK
ALTER TABLE dim_date_times
DROP CONSTRAINT date_uuid_pkey
ALTER TABLE dim_date_times
ADD CONSTRAINT date_uuid_pkey
PRIMARY KEY (date_uuid)

--CARD NUMBER PK
ALTER TABLE dim_card_details
DROP CONSTRAINT card_number_pkey
ALTER TABLE dim_card_details
ADD CONSTRAINT card_number_pkey
PRIMARY KEY (card_number)
