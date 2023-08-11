"""
Purpose: Illustrate addition of continuous information. 

This is a simple example that uses a deque to store the last 15 minutes of
temperature readings for three locations.

The data is updated every minute.

Continuous information might also come from a database, a data lake, a data warehouse, or a cloud service.

----------------------------
Open API Weather Information
-----------------------------

Go to: https://www.freeforexapi.com/

And sign up for your own free account and API key. 

The key should be kept secret - do not share it with others.
Open Weather API allows 1000 free requests per day.
That's about 125 per working hour, so comment it out when first testing. 

After everything works, and you have your own API key, uncomment it and use the real information.

-----------------------
Keeping Secrets Secret
-----------------------

Keep secrets in a .env file - load it, read the values.
Add the .env file to your .gitignore so you don't publish it to GitHub.
We usually include a .env-example file to illustrate the format.

"""
# Standard Library
import asyncio
import os
from collections import deque
from datetime import datetime
from pathlib import Path

# External Packages
import aiohttp
import pandas as pd
from dotenv import load_dotenv

# Local Imports
from fetch import fetch_from_url  # Implement fetch_from_url or use your own implementation
from util_logger import setup_logger

# Set up a file logger
logger, log_filename = setup_logger(__file__)

# ... (init_csv_file function remains unchanged) ...

async def fetch_from_url(url, params=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            return data

def get_API_key():
    # Keep secrets in a .env file - load it, read the values.
    # Load environment variables from .env file
    load_dotenv()
    key = os.getenv("OPEN_FOREX_API_KEY")
    return key

async def get_exchange_rates(access_key, source, currencies):
    logger.info("Calling get_exchange_rates")
    exchange_url = f"http://api.currencylayer.com/live"
    params = {
        "access_key": access_key,
        "source": source,
        "currencies": ",".join(currencies),
        "format": 1
    }
    
    response = await fetch_from_url(exchange_url, params=params)
    rates = response.get("quotes", {})
    
    return rates

async def update_csv_location():
    """Update the CSV file with the latest exchange rate information."""
    logger.info("Calling update_csv_location")
    try:
        access_key = get_API_key()  # Get your API key here
        source_currency = "GBP"
        target_currencies = ["USD", "AUD", "CAD", "PLN", "MXN"]
        
        num_updates = 10  # Number of updates to perform
        records_deque = deque(maxlen=num_updates)  # Deque to store most recent records

        fp = Path(__file__).parent.joinpath("data").joinpath("exchange_rates.csv")

        for _ in range(num_updates):  # To get num_updates readings
            new_rates = await get_exchange_rates(access_key, source_currency, target_currencies)
            
            # Convert exchange rates to float and replace None with 0
            new_record = {
                currency: int(rate) if rate is not None else 0
                for currency, rate in new_rates.items()
            }
            
            records_deque.append(new_record)

            # ... (rest of the function remains unchanged) ...

    except Exception as e:
        logger.error(f"ERROR in update_csv_location: {e}")

if __name__ == "__main__":
    load_dotenv()
    loop = asyncio.get_event_loop()
    task = loop.create_task(update_csv_location())
    
    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt detected. Cancelling tasks...")
        task.cancel()
        loop.run_until_complete(asyncio.gather(*asyncio.Task.all_tasks()))
    finally:
        loop.close()
