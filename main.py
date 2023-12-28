
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning


def user_data():
    """All methods used to connect to amazon database and return cleaned data for specific table to sql database"""
    # Connect to Amazon DB
    amazon_db_connector = DatabaseConnector('db_creds.yaml') 
    # Read DB Credentials to allow connection
    amazon_db_connector.read_db_creds()
    # Create engine for database connection
    amazon_db_connector.init_db_engine()
    # Get information from database
    amazon_db_connector.list_db_tables()
    # Extract data from Amazon DB and convert to pandas dataframe.
    db_extraction_dc = DataExtractor()
    table_name = 'legacy_users'
    db_cleaning_dc = DataCleaning(db_extraction_dc.read_rds_table(amazon_db_connector, table_name))
    # Clean the data
    cleaned_dataframe = db_cleaning_dc.clean_user_data() #dataframe
    # Connect to the sales_data database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection()
    # Upload cleaned dataframe to postgres database
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_users') #AttributeError: 'DatabaseConnector' object has no attribute 'engine'

def card_details():
    """All methods used to access data from pdf and return cleaned data to sql database"""
    # Extract data from pdf and return a Pandas dataframe
    db_extraction_dc = DataExtractor()
    card_details = db_extraction_dc.retrieve_pdf_data()
    # Clean the data
    pdf_cleaner = DataCleaning(card_details)
    cleaned_dataframe = pdf_cleaner.clean_card_details()
    # Upload cleaned dataframe to postgres database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_card_details')

def store_details():
    """All methods used to access data from API get requests and return cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    # Make API calls to get the number of stores the company owns
    num_stores = db_extraction_dc.list_number_of_stores(api_link="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", api_dict={"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"})
    #t Extract all data for each store
    stores_data = db_extraction_dc.retrieve_stores_data() #api_link="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
    # Clean the data 
    amazon_api_cleaner = DataCleaning(stores_data)   
    cleaned_dataframe = amazon_api_cleaner.clean_stores()
    # Upload cleaned dataframe to postgres database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_store_details') 

def product_details():
    """"All methods used to access data from s3 bucket and return cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    # Get data from S3 Bucket
    s3_data = db_extraction_dc.extract_from_s3(s3_bucket='data-handling-public', s3_key='products.csv')
    products_cleaner = DataCleaning(s3_data)
    # Clean the data
    cleaned_dataframe = products_cleaner.clean_products()
    # Upload cleaned dataframe to postgres database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_products') 

def orders_details():
    """All methods used to download the and clean orders table, will be single source of truth and main central connection point for star-based schema"""
    # Connect to Amazon DB
    amazon_db_connector = DatabaseConnector('db_creds.yaml') 
    # Read DB Credentials to allow connection
    amazon_db_connector.read_db_creds()
    # Create engine for database connection
    amazon_db_connector.init_db_engine()
    # Get information from database
    amazon_db_connector.list_db_tables()
    db_extraction_dc = DataExtractor()
    table_name = 'orders_table'
    db_cleaning_dc = DataCleaning(db_extraction_dc.read_rds_table(amazon_db_connector, table_name))
    # Clean the data
    cleaned_dataframe = db_cleaning_dc.clean_order_table()
    # Upload cleaned dataframe to postgres database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'orders_table') 

def date_details():
    """All methods used to extract data from json file in s3 bucket and upload cleaned data to sql database"""
    db_extraction_dc = DataExtractor()
    # Get data from S3 Bucket
    data = db_extraction_dc.extract_json_from_s3(url='https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')
    products_cleaner = DataCleaning(data)
    # Clean the data
    cleaned_dataframe = products_cleaner.clean_date_details()
    # Upload cleaned dataframe to postgres database
    sales_db_connector = DatabaseConnector('sql_creds.yaml')
    sales_db_connector.read_db_creds()
    sales_db_connector.init_sql_connection() 
    sales_db_connector.upload_to_db(cleaned_dataframe, 'dim_date_times') 


if __name__ == '__main__':
    user_data() #turn off data upload
    card_details() #turn off data upload
    store_details() #turn off data upload
    product_details() #turn off data upload
    orders_details() #turn off data upload
    date_details() #turn off data upload
