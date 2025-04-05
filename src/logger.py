## Logger is for the purpose that any execution  that happens we shud be able to log all those info 
# in some files so that we'll able  to track if there is some errors
# even the custom exception error or any other exception, we will try to log that in text file
import logging
import os 
import sys 
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d%(name)s-%(levelname)s-%(message)s",
    level=logging.INFO
    
)



## Whenever we get an exception i'll take that exception and log it with the logger
# file and logging.info and put it inside the file
