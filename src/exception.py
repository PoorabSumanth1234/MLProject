import sys 
import logging 
# Any exception that is getting controlled , the sys library is having that information

def error_message_details(error,error_detail:sys): # error detail present in sys i.e what module has been imported 
    _,_,exc_tb=error_detail.exc_info()   # not inteested to know the first two exceptions
    # this exc_info will give info about which file the exception occured or which line the exception occured. \
    file_name=exc_tb.tb_frame.f_code.co_filename  # to know this see the documentation 
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format   # how my msg shud look like in the file 
    file_name, exc_tb.tb_lineno,str(error)
    return error_message
    
    # this function will be called whenever my error raises 

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # overridden init method 
        self.error_message=error_message_details(error_message,error_detail=error_detail)
        # Whenever I raise my custom exception , it will inherit the parent exception. 
        # Whatever error msg is coming from error_message_details function that error message will come over and initialie the class variable  or the custom exception variable i.e error msg 
        # error_detail is tracked by sys 
        
    def __str__(self):
        return self.error_message
    
    
    
    