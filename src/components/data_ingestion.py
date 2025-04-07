# Data ingestion -- It means that I will be reading a dataset from a database or it can be from some other file location
# ## Initially, we need to read the database
# So, reading a data from a specific database is data injestion
# SO, data ingestion is also a component
# We divide the data into train and test and then validation data and etc. 

## THis will have the code that is related to reading the data 
# After data injestion come data transformation

import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass   # used to create class variables 
from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig
#from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer
@dataclass    # using dataclass ,we will able to directly define our class variable 
class DataIngestionConfig(): # in my data ingestion component any input that is required , I will give through data ingestion config
    train_data_path: str=os.path.join('artifacts',"train.csv")    # Data ingestion all outputs will be stored in this file path 
    test_data_path:str=os.path.join('artifacts',"test.csv")   # all outputs are stored in the artifact folder 
    raw_data_path:str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # The three paths will saved in this variable 
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('Notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")
            
            # Artifacts is a folder so we create  a folder wrt test data path, train data path  and raw data path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # i am getting the directory name wrt train_data_path by os.path.dirname
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) # save this to train_data_path artifact folder
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        ## We will pass these two paths so that my next phase i.e data transformation will be 
        # able to grab the information and take  all this data points and start the process.
        
        except Exception as e:
            raise CustomException(e,sys) 
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
## We can change the code and read from mongodb or mysql        
        
# We read the data from the dataset an then we  convert this to raw data path 
# and then train test split and then saved train and test files into 
# artifacts folder for my data transformation phase
       
        
    
    

