from fastapi import FastAPI
# from database_utils import DatabaseConnector
import boto3
import io
import numpy as np
import pandas as pd
import requests
import tabula

class DataExtractor():
    """
    Utility class to extract data from data sources like CSV files, an API and an S3 bucket. 
    Please see main.py to see how and when these methods are called. 
    """
    def read_rds_table(self, db_connector, table_name): 
        """
        Connects to database of data to be cleaned and returns information as a pandas dataframe. 

        Args:
            db_connector (database connection): database connection from init_db_engine method. 
            table_name (literal): name of table in database to be accessed. 
        Returns:
            legacy_data_frame (pd.dataframe): dataframe of data to be cleaned. 
        """
        db_connected = db_connector.engine.connect()
        legacy_data_frame = pd.read_sql_table(table_name, db_connected)
        DO_NOT_EDIT_copy_legacy_user_data_frame = legacy_data_frame.copy(deep=True)
        db_connected.close()
        return legacy_data_frame
    
    def retrieve_pdf_data(self):
        """"
        Exports data from a pdf hyperlink and returns a pandas dataframe with index column added and page headers removed. 
        
        Returns:
            card_details(pd.dataframe): dataframe of data from pdf. 
        """
        card_details = tabula.read_pdf("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf", pages='all')
        card_details = pd.concat(card_details)
        card_details.index = np.arange(0, len(card_details))
        # print(card_details)
        return card_details
    
    api = FastAPI()
    def list_number_of_stores(self, api_link, api_dict):
        """
        Reads data from API get request and returns the number of stores to be used in retrieve_stores_data method.  

        Args:
            api_link (literal): hyperlink to amazon database location. 
            api_dict (dict[strs]): access keys for amazon database. 
        Returns:
            num_stores: number of stores to get information for.  
        """
        self.api_dict = api_dict
        self.response = requests.get(api_link, headers=api_dict)
        print(self.response)
        self.num_stores = self.response.json().get('number_stores')
        return self.num_stores #451

    def retrieve_stores_data(self): # api_link
        """
        TODO: WORKING ON!
        Get data from API get requests for every store (the number returned in list_number_of_stores) and return pandas 
        dataframe of the store details.

        Args:
            stores_data(pd.dataframe): dataframe of all the stores information. 
        """
        data = []
        print('Gathering information for this request. Please wait...')
        for store_number in range(self.num_stores):
            # print(store_number)
            self.response = requests.get(f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}", headers=self.api_dict)
            data.append(self.response.json())       
        stores_data = pd.DataFrame(data)
        return stores_data
    
    def extract_from_s3(self, s3_bucket, s3_key):
        """
        Access CSV file from S3 object and returns a pandas dataframe of information. Must generate access key and configure AWS 
        beforehand to be able to run this. 

        Args:
            s3_bucket (literal): location of s3 bucket. 
            s3_key (literal): file name for specific s3 object. 
        """
        s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
            csv_content = response['Body'].read().decode('utf-8')
            product_data = pd.read_csv(io.StringIO(csv_content))
            return product_data
        except Exception as e:
            print('Error')

    def extract_json_from_s3(self, url):
        """
        Extract data from json file saved as an S3 object and return the information as pandas dataframe with index column added. 

        Args:
            url (literal): file path to json file. 
        """
        data = pd.read_json(url)
        data['index'] = range(0, len(data))
        # print(data)
        return data 

