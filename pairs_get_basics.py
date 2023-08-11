"""
Purpose: 

Provide basic non-reactive functions to support 
the MT Cars continuous intelligence and interactive analytics dashboard.

These functions can be used and tested independently of our Shiny app.

Keeping them separate makes our dashboard code cleaner and easier to read.
"""
# Python Standard Library 
import pathlib
import os

# External Packages
import pandas as pd  # pip install pandas

# Local Imports
from util_logger import setup_logger

# Set up a logger for this file (see the logs folder to help with debugging).
logger, logname = setup_logger(__name__)


def get_mtcars_df():
    """Return combined_data_with_currency pandas Dataframe."""
    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("combined_data_with_currency.csv")
    # logger.info(f"Reading data from {p}")
    df = pd.read_csv(p)
    return df


