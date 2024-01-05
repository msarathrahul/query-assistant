import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    # Extract information from the exception traceback
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Construct the error message with relevant details
    error_message = (
        f"Error occurred in Python script: {file_name}, "
        f"line number: {exc_tb.tb_lineno}, "
        f"error message: {str(error)}"
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class constructor with the provided error message
        super().__init__(error_message)
        # Generate a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        # Override the __str__ method to return the custom error message
        return self.error_message
