import os
import sys
from Respire.Logger import logging

def error_message_detail(error, error_detail:sys):
    # Retreiving TraceBack information
    # exc_info() returns a tuple - (Exception type, Exception value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    # Extracting file name, line number and error message
    file_name = exc_tb.tb_frame.f_code.co_filename
    ermsg = f"Error in Script: {file_name} - Line: {exc_tb.tb_lineno} - Message: {str(error)}" 
    logging.info(ermsg)
    return ermsg

class CustomException(Exception):
    def __init__(self, ermsg, error_detail):
        super().__init__(ermsg)
        self.error_message = error_message_detail(
            ermsg, error_detail=error_detail)

    def __str__(self):
        return self.error_message