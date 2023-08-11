"""
Purpose: Provide user interaction options for combined data with currency dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui
import pandas as pd
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Text, END, Scrollbar
from pathlib import Path
import matplotlib.pyplot as plt
import threading
import time

# Function to load the combined data and currency dataset
def load_data():
    combined_fp = "data/combined_data_with_currency.csv"
    currency_fp = "data/combined_data_with_currency.csv"
    combined_df = pd.read_csv(combined_fp)
    currency_df = pd.read_csv(currency_fp)

    return combined_df, currency_df

# Function to merge combined data with currency dataset based on IDs
def merge_data_with_currency(combined_df, currency_df):
    merged_df = pd.merge(combined_df, currency_df, on="ID")
    return merged_df

# Function to plot real-time updates for a currency pair
def plot_real_time_updates(currencypair_df):
    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot([], [])
    ax.set_xlabel("Update Time")
    ax.set_ylabel("Exchange Rate")
    ax.set_title(f"Real-Time Updates for Currency Pair: {currencypair_df['Pair'].iloc[0]}")

    def update_plot():
        while True:
            x = currencypair_df["Time"].tolist()
            y = currencypair_df["Rate"].tolist()
            line.set_xdata(x)
            line.set_ydata(y)
            ax.relim()
            ax.autoscale_view()
            plt.pause(1)

    threading.Thread(target=update_plot).start()

# Function to display last updates for selected currency pairs
def display_last_updates(selected_pairs, merged_df):
    selected_df = merged_df[merged_df["CurrencyPair"].isin(selected_pairs)]
    last_updates = selected_df.groupby("CurrencyPair").tail(10)
    return last_updates

# Function to display continuous updates for selected currency pairs
def display_continuous_updates(selected_pairs, merged_df):
    selected_df = merged_df[merged_df["CurrencyPair"].isin(selected_pairs)]
    while True:
        print("\nContinuous Updates for Selected Currency Pairs:")
        print(selected_df)
        time.sleep(5)  # Display updates every 5 seconds

# Function to handle the "Select" button action
def select_button_action():
    global selected_currency_var, selected_action_var  # Add this line
    selected_currency_pairs = selected_currency_var.get().split(",")
    selected_action = selected_action_var.get()

    if selected_action == "Last 10 Updates":
        updates = display_last_updates(selected_currency_pairs, merged_df)
        output_text.config(state="normal")
        output_text.delete("1.0", END)
        output_text.insert("end", updates.to_string(index=False))
        output_text.config(state="disabled")
    elif selected_action == "Continuous Updates":
        display_continuous_updates(selected_currency_pairs, merged_df)

# Main function to initialize the GUI
def main():
    global merged_df
    merged_df, _ = load_data()

    root = Tk()
    root.title("Currency Updates GUI")

    # Create and position widgets
    Label(root, text="Select Currency Pairs:").pack()
    currency_options = merged_df["CurrencyPair"].unique()
    selected_currency_var = StringVar(root)
    selected_currency_var.set(currency_options[0])
    currency_menu = OptionMenu(root, selected_currency_var, *currency_options)
    currency_menu.pack()

    Label(root, text="Select Action:").pack()
    action_options = ["Last 10 Updates", "Continuous Updates"]
    selected_action_var = StringVar(root)
    selected_action_var.set(action_options[0])
    action_menu = OptionMenu(root, selected_action_var, *action_options)
    action_menu.pack()

    select_button = Button(root, text="Select", command=select_button_action)
    select_button.pack()

    global output_text
    output_text = Text(root, wrap="none", state="disabled")
    output_text.pack()

    # Start GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
