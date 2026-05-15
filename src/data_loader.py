import yfinance as yf
import pandas as pd
import os

def download_data(tickers, start_date, end_date):
    # Adding USD/INR to the list to handle currency
    all_tickers = tickers + ["INR=X"]
    print(f"Downloading data for: {all_tickers}")
    
    # Downloading  data
    data = yf.download(all_tickers, start=start_date, end=end_date)
    
    # Checking if 'Adj Close' exists in the columns (MultiIndex handling)
    if 'Adj Close' in data.columns:
        data = data['Adj Close']
    elif 'Close' in data.columns:
        data = data['Close']
    
    # Saving raw data to the data folder
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/raw_data.csv')
    print("Data saved to data/raw_data.csv")
    return data

if __name__ == "__main__":
    test_stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    download_data(test_stocks, "2023-01-01", "2024-05-01") # Used 2024 data