
from sqlalchemy import create_engine, inspect
import yaml 


class DatabaseConnector():
    """
    Class to connect with and upload data to the database.
    Please see main.py to see how and when these methods are called. 
    """
    def __init__(self, yaml_file):
        """
        See help(DatabaseConnector) for more detail. 

        Args:
            yaml_file: connection details and passwords to connect to database. 
        """
        self.yaml_file = yaml_file

    def read_db_creds(self):
        """
        Reads and returns sensitive database connection credentials, called in the init_db_engine and init_sql_connection methods. 
        Yaml files added to git ignore file.

        Returns: 
            db_credentials: credentials to connect to a database. 
        """
        with open(self.yaml_file, 'r') as file:
            self.db_credentials = yaml.safe_load(file)
            return self.db_credentials

    def init_db_engine(self):
        """
        Read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine to get data from 
        Amazon database. 

        Returns:
            engine (engine): database connection to an Amazon database via a sqlalchemy engine. 
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = self.db_credentials['RDS_HOST']
        USER = self.db_credentials['RDS_USER']
        PASSWORD = self.db_credentials['RDS_PASSWORD']
        DATABASE = self.db_credentials['RDS_DATABASE']
        PORT = self.db_credentials['RDS_PORT']
        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
        return self.engine
    
    def init_sql_connection(self): 
        """
        Read the credentials from the return of read_db_creds and initalise sql connection to faciliate pushing cleaned data to pgadmin database. 

        Returns:
            engine (engine): database connection to pgAdmin via a sqlalchemy engine. 
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        database = self.db_credentials['DATABASE']
        user = self.db_credentials['USER']
        password = self.db_credentials['PASSWORD']
        host = self.db_credentials['HOST']
        port = self.db_credentials['PORT']
        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{user}:{password}@{host}/{database}")
        return self.engine

    def list_db_tables(self):
        """
        Use engine returned from init_db_engine to list all the tables in the database. 

        Returns:
            table_names (list[str]): list of table names in Amazon database. 
        """
        inspector = inspect(self.engine)
        self.table_names = inspector.get_table_names() #['legacy_store_details', 'legacy_users', 'orders_table']
        return self.table_names

    def upload_to_db(self, pd_dataframe, table_name):
        """
        Upload cleaned data to sql using engine from init_sql_connection method. 

        Args:
            pd_dataframe: dataframe to be uploaded to pgadmin.
            table_name: name that dataframe will be labelled as in pgadmin.
        """
        pd_dataframe.to_sql(name = table_name, con = self.engine, if_exists='replace')

