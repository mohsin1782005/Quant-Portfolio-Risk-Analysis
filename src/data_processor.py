import pandas as pd
import numpy as np
import os

def process_portfolio():
    # Loading raw data
    df = pd.read_csv('data/raw_data.csv', index_col=0, parse_dates=True)
    
    # Separate Stock Prices and FX Rate
    fx_rate = df['INR=X']
    stocks = df.drop(columns=['INR=X'])
    
    # FX Adjustment (Normalize all to a common base)
    # Since they are all in INR (NSE), we focus on the Portfolio Returns
    returns = stocks.pct_change().dropna()
    
    # Defining Portfolio Weights
    # assuming equal weights for now: 33% Reliance, 33% TCS, 33% Infosys
    weights = np.array([1/len(stocks.columns)] * len(stocks.columns))
    
    # 4. Calculating Portfolio Daily Return
    returns['Portfolio'] = returns.dot(weights)
    
    # Saving
    returns.to_csv('data/processed_returns.csv')
    print("Portfolio Returns calculated with Weights. Saved to data/processed_returns.csv")
    return returns

if __name__ == "__main__":
    process_portfolio()