import pandas as pd
import numpy as np

def calculate_risk_metrics():
    # Loading processed returns
    returns = pd.read_csv('data/processed_returns.csv', index_col=0, parse_dates=True)
    
    # Calculating Volatility (Standard Deviation)
    volatility = returns.std() * np.sqrt(252) # Annualized
    
    # Calculating Value at Risk (95% Confidence)
    var_95 = returns.quantile(0.05)
    
    # Creating a summary table
    risk_summary = pd.DataFrame({
        'Annualized_Vol': volatility,
        'VaR_95_Daily': var_95
    })
    
    risk_summary.to_csv('data/risk_metrics.csv')
    print("Risk Metrics calculated (Volatility & VaR). Saved to data/risk_metrics.csv")
    print(risk_summary)
    return risk_summary

if __name__ == "__main__":
    calculate_risk_metrics()
