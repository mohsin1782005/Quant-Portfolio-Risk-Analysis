import pandas as pd
import numpy as np
from scipy.stats import norm

def calculate_advanced_risk(confidence_level=0.95):
    # Loading processed returns
    returns = pd.read_csv('data/processed_returns.csv', index_col=0, parse_dates=True)
    port_returns = returns['Portfolio']
    
    # Historical Simulation
    h_var = np.percentile(port_returns, (1 - confidence_level) * 100)
    h_es = port_returns[port_returns <= h_var].mean()
    
    # Parametric (Normal Distribution)
    mu = port_returns.mean()
    sigma = port_returns.std()
    p_var = norm.ppf(1 - confidence_level, mu, sigma)
    # Formula for Normal ES
    p_es = mu - sigma * (norm.pdf(norm.ppf(1 - confidence_level)) / (1 - confidence_level))
    
    # Summary
    metrics = pd.DataFrame({
        'Method': ['Historical', 'Parametric'],
        'VaR_95': [h_var, p_var],
        'Expected_Shortfall': [h_es, p_es]
    })
    
    metrics.to_csv('data/advanced_risk_metrics.csv', index=False)
    print("Risk Metrics Calculated:")
    print(metrics)
    return metrics

if __name__ == "__main__":
    calculate_advanced_risk()