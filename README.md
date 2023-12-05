# Multinational Retail Data Centralisation

## Project description:
Training project to gather different data sources from Amazon Web Services (AWS) databases and S3 objects like pdfs, csv files, json files. Once the information is gathered it must be cleaned and pushed to one central database in PostgreSQL to be analysed. 

## Installation instructions:
Made using Python 3.11.6 and VS Code 1.84 and pgAdmin4 7.5

Imports used: 
* database_utils.py: sqlalchemy, yaml
* data_extraction.py: FastAPI, boto3, io, numpy, pandas, requests, tabula
* data_cleaning.py: datetime, calendar, string
    
* Clone repo: git clone https://github.com/CJ1608/Multinational-Retail-Data-Centralisation.git

Install imports:
* SQLAlchemy https://pypi.org/project/SQLAlchemy/
* boto3 https://pypi.org/project/boto3/
* numpy https://pypi.org/project/numpy/
* pandas https://pypi.org/project/pandas/
* requests https://pypi.org/project/requests/
* tabula https://pypi.org/project/tabula-py/

## File structure:
* README.md
* .gitignore
* LICENSE
* data_cleaning.py
* data_extraction.py
* database_utils.py
* main.py: main file that calls methods from the 3 python files above.
* requirements: packages and versions
   * sql_files (T1-7: altering data types, T8-9: setting primary and foreign keys)
        * T1 orders table.sql
        * T2 dim users table.sql
        * T3 dim store details.sql
        * T4 dim products.sql
        * T6(no5) dim date times.sql
        * T7 dim card details.sql
        * T8.sql
        * T9.sql
    * sql_data_queries (SQL querys)
        * data_queries.sql

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
