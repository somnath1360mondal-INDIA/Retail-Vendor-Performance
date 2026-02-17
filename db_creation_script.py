import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    filemode = "a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = 'False')     # append for increamental load

def load_raw_data():
    start = time.time()
    
    try:
        for file in os.listdir(data_path):
            if file.endswith(".csv"):
                file_path = os.path.join(data_path, file)
                
                try:
                    df = pd.read_csv(file_path)
                    logging.info(f"{file} loaded successfully with shape {df.shape}")
                    
                    ingest_db(df, file[:-4], engine)
                    logging.info(f"{file} ingested into database successfully")
                
                except Exception as e:
                    logging.error(f"Error processing file: {file}", exc_info=True)
        
        logging.info("Ingestion Completed Successfully")
    
    except Exception as e:
        logging.critical("Fatal error in load_raw_data function", exc_info=True)
    
    finally:
        end = time.time()
        total_time = (end - start) / 60
        logging.info(f"Total Time Taken: {total_time:.2f} minutes")

if __name__ == '__main__':
    load_raw_data()