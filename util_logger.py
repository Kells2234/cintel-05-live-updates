"""
Purpose: Set up logging once and reuse it. 

Author: Denise Case

This file automatically records your work so you don't have to. 
Analysts and data scientists will work hard once, to be lazy later.
You should be able to reuse this code without modification.
You're also welcome to use it as a template for your own logging. 

"""

import logging
import pathlib
import platform
import sys
import os
import datetime
import pandas as pd
import glob
import os

# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='data_processing.log')


def get_source_directory_path(current_file):
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(current_file))
    return dir


def setup_logger(current_file):
    """Setup a logger to automatically log useful information.
    @param current_file: the name of the file requesting a logger.
    @returns: the logger object and the name of the logfile.
    """
    logs_dir = pathlib.Path("logs")
    logs_dir.mkdir(exist_ok=True)

    module_name = pathlib.Path(current_file).stem
    log_file_name = logs_dir.joinpath(module_name + ".log")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Set the root logger level.

    # Create file handler which logs even debug messages.
    file_handler = logging.FileHandler(log_file_name, "w")
    file_handler.setLevel(logging.DEBUG)

    # Create console handler with a higher log level.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers.
    formatter = logging.Formatter("%(asctime)s.%(name)s.%(levelname)s %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger.
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    divider_string = "============================================================="
    python_version_string = platform.python_version()
    today = datetime.date.today()

    logger.info(divider_string)
    logger.info(f"Today is {today} at {datetime.datetime.now().strftime('%I:%M %p')}")
    logger.info(
        f"This file is running on: {os.name} {platform.system()} {platform.release()}"
    )
    logger.info(f"The Python version is: {python_version_string}")
    logger.info(f"The active environment path is:   {sys.prefix}")
    logger.info(f"The current working directory is: {os.getcwd()}")
    logger.info(divider_string)

    return logger, log_file_name


if __name__ == "__main__":
    logger, logname = setup_logger(__file__)
    logger.info("Starting util_logger.py")
    logger.info(f"Information is logged to: logs/{logname}")
    logger.info("Ending util_logger.py")

    # Use built-in open() function to read log file and print it to the terminal
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())