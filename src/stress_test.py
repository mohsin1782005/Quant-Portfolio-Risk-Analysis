import pandas as pd
import numpy as np

def run_stress_test():
    # Loading advanced risk metrics to compare
    returns_df = pd.read_csv('data/processed_returns.csv', index_col=0, parse_dates=True)
    current_val = 1000000 # Assuming a 1 Million INR Portfolio
    
    # Defining Scenarios
    scenarios = {
        'Normal Day (Mean)': returns_df['Portfolio'].mean(),
        'Market Crash (-15%)': -0.15,
        'Currency Crisis (+5% USD/INR)': -0.05, # INR weakens
        'Combined Extreme Event': -0.20
    }
    
    stress_results = pd.DataFrame({
        'Scenario': scenarios.keys(),
        'Return_Impact': scenarios.values(),
        'Portfolio_Value_Loss': [current_val * r for r in scenarios.values()]
    })
    
    stress_results.to_csv('data/stress_test_results.csv', index=False)
    print("Stress Testing Complete. Results saved to data/stress_test_results.csv")
    print(stress_results)
    return stress_results

if __name__ == "__main__":
    run_stress_test()