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

from tkinter import Tk, Label, Button, OptionMenu, StringVar, Text, END, Scrollbar
import threading
import time
import pandas as pd
import os

# Sample data fetching function (replace with your data fetching logic)
def fetch_currency_data(currency_pair):
    # Replace this with your actual data fetching logic
    new_data = {
        "Pair": currency_pair,
        "Price": 1.2345,  # Sample price
        "Time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return new_data

def update_csv_with_new_data(new_data):
    csv_file = "combined_data_with_currency.csv"  # Update with your CSV file path
    df = pd.DataFrame([new_data])
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode="a", header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)

def main():
    root = Tk()
    root.title("Currency Pair Data")

    selected_currency_var = StringVar(root)
    selected_currency_var.set("GBPUSD")  # Default currency pair
    currency_options = ["GBPUSD", "EURUSD", "USDJPY"]  # Add more options
    currency_menu = OptionMenu(root, selected_currency_var, *currency_options)
    currency_menu.pack()

    def update_data():
        selected_currency = selected_currency_var.get()
        new_data = fetch_currency_data(selected_currency)
        update_csv_with_new_data(new_data)
        data_text.insert(END, f"Updated data for {selected_currency}: {new_data}\n")

    update_button = Button(root, text="Update Data", command=update_data)
    update_button.pack()

    data_text = Text(root)
    data_text.pack()

    def update_data_continuously():
        try:
            while True:
                selected_currency = selected_currency_var.get()
                new_data = fetch_currency_data(selected_currency)
                update_csv_with_new_data(new_data)
                data_text.insert(END, f"Continuous update for {selected_currency}: {new_data}\n")

                # Wait for update_interval seconds before the next update
                update_interval = 60
                time.sleep(update_interval)

        except Exception as e:
            data_text.insert(END, f"ERROR: {e}\n")

    data_update_thread = threading.Thread(target=update_data_continuously)
    data_update_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()