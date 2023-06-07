"""logger is used to  tracking events that happen when some software runs"""

import logging
from scripts.constants.app_constants import loggers


def getLogger():
    """
    :tracking every function
    """
    __logger__ = logging.getLogger("")
    __logger__.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s')

    file_handler = logging.FileHandler(loggers.File_name_logger)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    __logger__.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    __logger__.addHandler(console_handler)

    return __logger__


logger = getLogger()
