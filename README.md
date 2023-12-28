# Multinational Retail Data Centralisation

## Project description:
Project to gather information, clean it and publish it in one central PostgresQL database. Data sources included an Amazon Web Services (AWS) databases and S3 objects like pdfs, csv files, json files.

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
