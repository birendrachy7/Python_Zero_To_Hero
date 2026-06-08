import logging

logging.basicConfig(
    level=logging.DEBUG,
    # format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

def divide_numbers(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.info(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        raise

try:
    divide_numbers(10, 5)
except ZeroDivisionError:
    # logging.critical("Application caught a division by zero error")
    print("Cannot divide by zero.")