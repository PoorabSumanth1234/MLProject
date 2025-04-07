## This includes how to change category features to numeric features
# How to handle OHE , LE 
## After this , we will do model training 

import sys 
import os
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
# Column transformer is used to create a pipeline
from sklearn.impute import SimpleImputer
# We can do multiple imputation techniques
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.utils import save_object

from src.exception import CustomException
from src.logger import logging

class DataTransformationConfig:   # This will give me the inputs that are required for my data transformation
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')              
# If we want to create any models and I want to save that into a pickle file for that we require some path

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformer_obj(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')), #handling missing values
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )  
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')), # handling missing values
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                    
                    
                ]
            )
            logging.info("Standard Scaling of numerical columns completed")
            logging.info("Categorical columns encoding completed")
            
            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                    
                    
                ]
            )
            # Column Transformer is combinaton of numerical and categorical pipeline
            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_obj()
            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]
            
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info(f"Applying preprocessing object on test dataframe and train dataframe")
            
            input_feature_train_array=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array=preprocessing_obj.transform(input_feature_test_df)
            
            train_arr= np.c_[input_feature_train_array,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_array,np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing objects")
            
            save_object(                              
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            # Used to save in pkl file 
            # Where to write the function save_objects , we will write in utils 
            # Utils will have  all the common functionalities which we can use for entire project
            
            return(train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path)
        
        except Exception as e:
            raise CustomException(e,sys)
          
        
        # get_data_transformer_obj is Used to create my pickle files which will be responsible in converting my 
       # categorical features to numerical and and if we want to perform StandardScaler etc
       
                

