import sys
from src.logger import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def error_message_detail(error, error_detail: sys):
    """Extracts error details including file name and line number."""
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exec_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """Custom exception class that provides detailed error messages."""
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=2/0
    except Exception as e:
        logging.info('error has occured')
        raise CustomException(e,sys)


