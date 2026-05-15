import os
from src.data_loader import download_data
from src.data_processor import process_portfolio
from src.advanced_risk import calculate_advanced_risk
from src.regime_detection import detect_regimes
from src.volatility_forecast import forecast_volatility
from src.risk_classification import classify_risk
from src.stress_test import run_stress_test
from src.visualizer import generate_visuals

def run_full_pipeline():
    print("Starting Quantitative Risk Analysis Pipeline...")
    
    # 1. Download
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    download_data(tickers, "2023-01-01", "2024-05-01")
    
    # 2. Process
    process_portfolio()
    
    # 3. Math & Stats
    calculate_advanced_risk()
    detect_regimes()
    
    # 4. Forecasting & ML
    forecast_volatility()
    classify_risk()
    
    # 5. Stress Testing
    run_stress_test()
    
    # 6. Final Dashboard
    generate_visuals()
    
print("\n" + "="*50)
print("FINANCIAL RISK ANALYSIS FRAMEWORK: COMPLETED")
print("="*50)
print("All quantitative datasets are available in the /data folder.")
print("Professional visualizations have been generated in /outputs.")
print("="*50)

if __name__ == "__main__":
    run_full_pipeline()