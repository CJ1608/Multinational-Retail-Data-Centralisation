# Multinational Retail Data Centralisation

## Project description:
Project to gather information, clean it and publish it in one central PostgresQL database. Data sources included an Amazon Web Services (AWS) databases and S3 objects like pdfs, csv files, json files.

## Breakdown of Project: 

### Extract Data
The data was extracted from different sources. Some of the information came from an Amazon Web Services database which involved connecting to the database using a SQLAlchemy engine. Some information was extracted using get API calls. The rest of the information came from S3 objects that ranged from pdfs, csv and json files which all needed to be extracted differently. 

### Clean Data 
The extracted data needed to be cleaned by doing certain tasks like removing null rows, converting the dates into the correct ISO8601 format and checking that non-null rows contained the correct information by checking the country code and other columns with standardised values. This helped to ensure that the information was clean, improving the data quality without losing too many records. It also made it easier to explore trends and get insights into the data. 

### Upload Data 
Once the data had been uploaded to PostgresQL, each column had to be cast to the correct data type and the primary and foreign keys created to establish the star-based schema. A star based schema is based on the idea of one central fact table and multiple dimension or 'dim' tables that all have a column that connects to a column in the fact table. 

### SQL Queries
Some of SQL Queries performed were:
![image](https://github.com/CJ1608/Multinational-Retail-Data-Centralisation/assets/128046995/09aa8da2-7cbd-44d0-831b-9282334b91c6)

![image](https://github.com/CJ1608/Multinational-Retail-Data-Centralisation/assets/128046995/18a6f180-58fb-483d-8a0d-91e1f6ae87e6)

## Installation instructions:
Made using Python 3.11.6 and VS Code 1.84 and pgAdmin4 7.5
* Check have all needed modules and packages installed. 
* Clone repo: git clone https://github.com/CJ1608/Multinational-Retail-Data-Centralisation.git

## File structure:
* LICENSE
* README.md
* data_cleaning.py
* data_extraction.py
* database_utils.py
* main.py
* requirements
* sql_files:
     * Dim Card Details
     * Dim Date Times
     * Dim Products
     * Dim Store Details
     * Dim Users Table
     * Foreign Keys
     * Orders Table
     * Primary Keys
     * SQL Queries

## Required Imports:
* SQLAlchemy https://pypi.org/project/SQLAlchemy/
* boto3 https://pypi.org/project/boto3/
* numpy https://pypi.org/project/numpy/
* pandas https://pypi.org/project/pandas/
* requests https://pypi.org/project/requests/
* tabula https://pypi.org/project/tabula-py/
  
## License information:
Distributed under the MIT License. See LICENSE for more information. 

## Acknowledgements:
* AiCore
* https://choosealicense.com/

## Learning resources used:
### Postgres
https://www.postgresqltutorial.com/ 

### S3 connection and boto3
* https://realpython.com/python-boto3-aws-s3/ 
* https://www.freecodecamp.org/news/read-csv-file-from-s3-bucket-in-aws-lambda/ 

### SQL Alchemy 
https://docs.sqlalchemy.org/en/20/core/engines.html 
