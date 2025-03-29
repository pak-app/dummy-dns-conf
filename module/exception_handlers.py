import logging
from functools import wraps
import os

# Configure logger
logger = logging.getLogger(os.getenv('APP_LOG_NAME'))
# logging.basicConfig(level=logging.INFO)

# This decorator handles the exception of DbsControllers' methods
def handle_exceptions(
    successful_message,
    error_message
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            try:
                result = func(*args, **kwargs)
                # Check if successful_message is not empty
                if not successful_message is None:
                    # See the function structure for more information about its logic
                    _handle_dynamic_string_formatting(successful_message, *args, **kwargs)
                return result
            
            except Exception as error:
                logger.error(f'{error_message}\nError ==> {error}')
        
        return wrapper
    return decorator

# It is check if dynamic string formatting is available
# If it is available, i will put the value on it
# If it is not it will logs the common message
def _handle_dynamic_string_formatting(message:str, *args, **kwargs) -> None:
    try: 
        formatted_message = message.format(*args, **kwargs)
        logger.info(formatted_message)
    except Exception as error:
        logger.info(message)