SELECT * FROM orders_table

--DATE UUID FK
-- ALTER TABLE orders_table
-- ADD CONSTRAINT date_uuid_fk
-- FOREIGN KEY (date_uuid)
-- REFERENCES dim_date_times(date_uuid)
-- ON DELETE NO ACTION
-- ON UPDATE NO ACTION;

-- USER-UUID FK
-- ALTER TABLE orders_table
-- ADD CONSTRAINT user_uuid_fk
-- FOREIGN KEY (user_uuid)
-- REFERENCES dim_users(user_uuid)
-- ON DELETE NO ACTION
-- ON UPDATE NO ACTION;

--CARD NUMBER FK
-- ALTER TABLE orders_table
-- ADD CONSTRAINT card_number_fkey
-- FOREIGN KEY (card_number)
-- REFERENCES dim_card_details(card_number)
-- ON DELETE NO ACTION
-- ON UPDATE NO ACTION;

-- STORE CODE FK
-- ALTER TABLE orders_table
-- ADD CONSTRAINT store_code_fkey
-- FOREIGN KEY (store_code)
-- REFERENCES dim_store_details(store_code)
-- ON DELETE NO ACTION
-- ON UPDATE NO ACTION;

--PRODUCT CODE FK
-- ALTER TABLE orders_table
-- ADD CONSTRAINT product_code_fkey
-- FOREIGN KEY (product_code)
-- REFERENCES dim_products(product_code)
-- ON DELETE NO ACTION
-- ON UPDATE NO ACTION;