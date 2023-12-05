
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning


def task3():
    """All methods used to connect to amazon database and return cleaned data for specific table to sql database"""
    amazon_db_connector = DatabaseConnector('db_creds.yaml') # connect to amazon db
    #task 3 step 2- read dredentials for db to access datavbase
    amazon_db_connector.read_db_creds()
    #task 3 step 3- create engine for database connection
    amazon_db_connector.init_db_engine()
    #task 3 step 4- get information from database
    amazon_db_connector.list_db_tables()
    # task 3 step 5 - extract data from amazon bd and put in pandas df. clean the amazon db and save as new dataframe
    db_extraction_dc = DataExtractor()
    table_name = 'legacy_users'
    db_cleaning_dc = DataCleaning(db_extraction_dc.read_rds_table(amazon_db_connector, table_name))
    # task 3 step 6- clean data
    cleaned_dataframe = db_cleaning_dc.clean_user_data() #dataframe
    # task 3 step 7- connect to the sales_data database (new DatabaseConnector)
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection()
    # task 3 step 8 - upload amazon database (users data) to sales db.
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_users') #AttributeError: 'DatabaseConnector' object has no attribute 'engine'

def task4():
    """All methods used to access data from pdf and return cleaned data to sql database"""
    #task 4, step 2 extract data and return as dataframe
    db_extraction_dc = DataExtractor()
    card_details = db_extraction_dc.retrieve_pdf_data()
    #task 4, step 3 clean data
    pdf_cleaner = DataCleaning(card_details)
    cleaned_dataframe = pdf_cleaner.clean_card_details()
    #task 4, step 4 upload clean data
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_card_details')

def task5():
    """All methods used to access data from API get requests and return cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    # task 5 step 1-2
    num_stores = db_extraction_dc.list_number_of_stores(api_link="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", api_dict={"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"})
    #task 5 step 3- extract all data from data source
    stores_data = db_extraction_dc.retrieve_stores_data() #api_link="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
    #task 5 step 4- clean data 
    amazon_api_cleaner = DataCleaning(stores_data)   
    cleaned_dataframe = amazon_api_cleaner.clean_stores()
    # task 5, step 5- upload database to table
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_store_details') 

def task6():
    """"All methods used to access data from s3 bucket and return cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    #step 1 get data from s3
    s3_data = db_extraction_dc.extract_from_s3(s3_bucket='data-handling-public', s3_key='products.csv')
    products_cleaner = DataCleaning(s3_data)
    #step 3 - clean all data
    cleaned_dataframe = products_cleaner.clean_products()
    #step 4- upload database to table
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_products') 

def task7():
    """All methods used to download the and clean orders table, will be single source of truth and main central connection point for star-based schema"""
    amazon_db_connector = DatabaseConnector('db_creds.yaml') # connect to amazon db
    #task 7 step 1- read credentials for db to access datavbase
    amazon_db_connector.read_db_creds()
    #create engine for database connection
    amazon_db_connector.init_db_engine()
    #task 7, step 2 get information from database
    amazon_db_connector.list_db_tables()
    db_extraction_dc = DataExtractor()
    table_name = 'orders_table'
    db_cleaning_dc = DataCleaning(db_extraction_dc.read_rds_table(amazon_db_connector, table_name))
    #task 7- 3 clean orders table data
    cleaned_dataframe = db_cleaning_dc.clean_order_table()
    #task 4, step 4- upload cleaned data
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'orders_table') 

def task8():
    """All methods used to extract data from json file in s3 bucket and upload cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    #step 1 get data from s3
    data = db_extraction_dc.extract_json_from_s3(url='https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')
    products_cleaner = DataCleaning(data)
    # #step 3 - clean all data
    cleaned_dataframe = products_cleaner.clean_date_details()
    # #step 4- upload database to table
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_date_times') 


if __name__ == '__main__':
    # task3() #turn off data upload
    # task4() #turn off data upload
    # task5() #turn off data upload
    # task6() #turn off data upload
    # task7() #turn off data upload
    # task8() #turn off data upload
    pass