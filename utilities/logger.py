import inspect
import logging
import time


def custom_logger(loglevel=logging.DEBUG):
    # Set class / method name from where it is called
    logger_name = inspect.stack()[1][3]

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(loglevel)

    curr_time = time.strftime("%m_%d_%Y_%H:%M:%S").replace(":", "_")
    log_file_name = '/Users/admin/Desktop/SDET1/sdet1_nop_commerce_pageobject/logs/log' + curr_time + '.log'
    fh = logging.FileHandler(log_file_name)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    # Add formatter to console or file handler
    fh.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(fh)
    return logger
