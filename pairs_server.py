""" 
Purpose: Provide continuous and reactive output for the combined data with currency dataset.

- Use inputs from the UI drop down menu to filter the dataset.
- Update reactive outputs in the UI Main Panel.
"""


# Standard Library
import asyncio
from datetime import datetime
from pathlib import Path
import os
from random import randint
from collections import deque
from dotenv import load_dotenv
import threading
import time

# External Libraries
import pandas as pd
import requests
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Text, END, Scrollbar
import matplotlib.pyplot as plt
import plotly.express as px

# Local Imports
from fetch import fetch_from_url
from pairs_ui_inputs import load_data
from util_logger import setup_logger
from shiny import render, reactive
from shinywidgets import render_widget

# Set up a file logger
logger, log_filename = setup_logger(__file__)

# Load environment variables from .env file
load_dotenv()

# Global variables
csv_locations = Path(__file__).parent.joinpath("data").joinpath("combined_data_with_currency.csv")

# ... (other functions)

# Define missing variables
reactive_currency = reactive.Value("GBPUSD")  # Default currency pair

def fetch_currency_data(currency_pair):
    # Replace with your API endpoint and access key
    api_url = f"http://api.example.com/exchange_rates"
    params = {
        "access_key": "YOUR_ACCESS_KEY",
        "currency_pair": currency_pair,
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extract the relevant data from the API response
        exchange_rate = data["exchange_rate"]
        timestamp = data["timestamp"]

        return {
            "Pair": currency_pair,
            "ExchangeRate": exchange_rate,
            "Timestamp": timestamp,
        }
    else:
        # Handle error cases
        return None

# ... (other functions)

# Main function to initialize the GUI and data updates
def main():
    global merged_df
    merged_df, _ = load_data()

    # Create a ShinyApp instance
    app = ShinyApp()

    # ... (previous UI setup)

    # Start data updates in a separate thread
    data_update_thread = threading.Thread(target=update_data_continuously)
    data_update_thread.start()

    # Start the ShinyApp event loop
    app.run()

def update_data_continuously():
    """Update the data file with the latest updates."""
    try:
        while True:
            # Fetch new data and update the CSV file
            new_data = fetch_currency_data(reactive_currency.get())  # Use the selected currency pair
            update_csv_with_new_data(new_data)
            logger.info("Updated data file with new currency updates")

            # Wait for update_interval seconds before the next update
            update_interval = 60
            time.sleep(update_interval)

    except Exception as e:
        logger.error(f"ERROR in update_data_continuously: {e}")

if __name__ == "__main__":
    main()
