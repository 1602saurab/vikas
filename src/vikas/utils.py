import os 
import sys 
from src.vikas.exception import CustomException 
from src.vikas.logger import logging 
import pandas as pd 
from dotenv import load_dotenv 
load_dotenv() 
import pymysql 

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db') 

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb= pymysql.connect(
            host=host,
            user=user,
            password=password,
            db = db
        )
        logging.info("Connection Established" , mydb)  
        df = pd.read_sql_query('Select * from placement',mydb)
        print(df.head())
        return df 
    except Exception as ex:
        raise CustomException(ex)