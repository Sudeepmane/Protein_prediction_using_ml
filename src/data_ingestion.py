import os
import sys
from exception import CustomException
from logger import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    data_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Entered the data ingestion method")
        try:
            df=pd.read_csv("C:\ML_Projects\protein_project\Data\protein.csv")
            logger.info("Read the dataframe succesfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.data_data_path,index=False,header=True)
            logger.info("Train test Split initiated")
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=35)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info("ingestion of the data is completed ")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()