"""
Store the last 15 minutes of stock values for several companies

Information is updated once per minute.
"""



# Import from Standard Library
import asyncio
import os
from pathlib import Path
from datetime import datetime
from random import randint

# Import external packages
import pandas as pd
import yfinance as yf
from collections import deque

# Local imports
from util_logger import setup_logger
from fetch import fetch_from_url

# Set up logger
logger, log_filename = setup_logger(__file__)

import pandas as pd
import glob
import os

# List all CSV files in a directory
csv_files = glob.glob("D:\Kelly's Education Folder\Continuous Intelligence/*.csv")

# Create an empty list to store data from all CSV files
dataframes = []

# Loop through each CSV file and read relevant columns into a DataFrame
for csv_file in csv_files:
    # Extract currency pair from file name (adjust this based on your file naming convention)
    currency_pair = os.path.splitext(os.path.basename(csv_file))[0]
    
    df = pd.read_csv(csv_file, usecols=["Date", "Price", "Open", "High", "Low", "Change %"])
    
    # Add a new column for currency pair
    df["CurrencyPair"] = currency_pair
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("combined_data_with_currency.csv", index=False)

# Print the first few rows of the combined DataFrame
print(combined_df.head(10))