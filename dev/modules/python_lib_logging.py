import logging
import python_lib_logging_empl

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
fileHandler = logging.FileHandler("logfile.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logger.exception("Cannot divide by zero!")
    else:
        return result

# Perform operations and log results
sum_result = add(10, 2)
logger.debug(f"Sum of the numbers is {sum_result}")

subtract_result = subtract(10, 2)
logger.debug(f"Difference of the numbers is {subtract_result}")

multiply_result = multiply(10, 2)
logger.debug(f"Product of the numbers is {multiply_result}")

divide_result = divide(10, 0)
if divide_result is not None:
    logger.debug(f"Quotient of the numbers is {divide_result}")

print(f"EOF..EOF...EOFEOF..EOF...EOFEOF..EOF...EOFEOF..EOF...EOFEOF..EOF...EOF")
