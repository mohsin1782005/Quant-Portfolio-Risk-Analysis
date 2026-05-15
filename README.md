# Quantitative Time-Series Risk Analysis Framework

## 📌 Project Overview
This project implements a dynamic, regime-aware portfolio risk modeling framework as per the thesis requirements. It integrates statistical validation, time-series forecasting, and machine learning to measure downside risk.

## 🚀 Key Features Implemented
* **FX-Adjusted Data:** Live NSE data (Reliance, TCS, INFY) adjusted for USD/INR.
* **Coherent Risk Metrics:** Historical and Parametric Value at Risk (VaR) & Expected Shortfall (ES).
* **Regime Detection:** K-Means Clustering to identify High/Low volatility market states.
* **Volatility Forecasting:** ARIMA (1,1,1) model for time-series risk prediction.
* **ML Classification:** Random Forest Classifier for risk state prediction.
* **Stress Testing:** Scenario analysis for market crashes and currency shocks.
* **Visualization:** High-resolution dashboard for thesis inclusion.

## 🛠️ How to Run
1. Ensure Python 3.10+ is installed.
2. Install dependencies:
   `pip install yfinance pandas numpy matplotlib seaborn scikit-learn statsmodels`
3. Run the master pipeline:
   `python main.py`

## 📂 Folder Structure
* `/src`: Modular Python scripts for each methodology.
* `/data`: CSV files containing raw and processed analytical data.
* `/outputs`: Professional charts and ML classification reports.
