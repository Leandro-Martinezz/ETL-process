import pandas as pd
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#settings for the sql server engine
SERVER_NAME = 'LEANDRO' 
DATABASE_NAME = 'DogsDB' 
ODBC_DRIVER = 'ODBC Driver 17 for SQL Server' 
USER = 'sa' 
PASSWORD = 'admin123' 

db_connection_string = ( 
    f'mssql+pyodbc://{USER}:{PASSWORD}@{SERVER_NAME}/'
    f'{DATABASE_NAME}'
    f'?driver={ODBC_DRIVER}')


def load(clean_data, table_name=None,): #this function load the previous transformed df in a sql server database
    logging.info("STARTING THE LOAD MODULE")
    engine = create_engine(db_connection_string) #create the engine connection
    logging.info(f"Starting the loading phase in table '{table_name}' in SQL Server.")
    
    try: #This block sets the loading parameters 
        clean_data.to_sql(table_name, 
                      con = engine,
                      if_exists="replace",
                      index=False,
                      index_label=None,)
        logging.info(f"Data loaded successfully in table '{table_name}'.")
        
        df_rows = clean_data.shape[0] #number of rows in transformed df
        db_table_rows = pd.read_sql(f"SELECT COUNT(*) FROM {table_name}", con=engine).iloc[0, 0] #quering for number of rows loaded
        if db_table_rows == df_rows: #checking if these are equals
            logging.debug(f"The number of rows in the df and the database table are equals" )
        else: 
            logging.warning(f"The number of rows in the df and the database table are not equals" ) 
        logging.info("THE LOAD MODULE HAS FINISHED")
        return True

    except Exception as e:
        logging.error(f"Error during loading phase: {e}")
        return False
    
    
   

    
