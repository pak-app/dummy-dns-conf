import logging
from functools import wraps
import os

# Configure logger
logger = logging.getLogger(os.getenv('APP_LOG_NAME'))
# logging.basicConfig(level=logging.INFO)

# This decorator handles the exception of DbsControllers' methods
def handle_exceptions(
    successful_message:str =None,
    error_message:str =None
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict[str, any]):
            
            try:
                result = func(*args, **kwargs)
                # Check if successful_message is not empty
                if not successful_message is None:
                    # See the function structure for more information about its logic
                    # *args[1:] is because of self of methods, if method has a param like name,
                    # *args will be like this (<Object blau, blau, blau...>, 'value of name')
                    _handle_dynamic_string_formatting(successful_message, *args[1:], **kwargs)
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
    except Exception:
        logger.info(message)