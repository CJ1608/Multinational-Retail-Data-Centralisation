-- Cast columns to correct data type

SELECT MAX(LENGTH(dim_date_times.month))
FROM dim_date_times --returns 2
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE varchar(2)

SELECT MAX(LENGTH(dim_date_times.year))
FROM dim_date_times --returns 4
ALTER TABLE dim_date_times
ALTER COLUMN year TYPE varchar(4)

SELECT MAX(LENGTH(dim_date_times.day))
FROM dim_date_times --returns 2
ALTER TABLE dim_date_times
ALTER COLUMN day TYPE varchar(2)

SELECT MAX(LENGTH(dim_date_times.time_period))
FROM dim_date_times --returns 10
ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE varchar(10)

ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE UUID
USING date_uuid::UUID
