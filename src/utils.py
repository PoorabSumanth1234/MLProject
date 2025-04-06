## Like if I want to read dataset from a database , I can create cliet like MongodB client
# If I want to save my model into the cloud , I can write the code in utils 

import os
import sys
import numpy as np
import pandas as pd 
from src.exception import CustomException
import dill    # helps in creating the pickle file 

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
            # When we use  dump obj will be saved in the specific file_path
    except Exception as e:
        raise CustomException(e,sys)
    
            