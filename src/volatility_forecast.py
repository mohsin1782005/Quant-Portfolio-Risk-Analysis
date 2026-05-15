import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.filterwarnings("ignore")

def forecast_volatility():
    # Loading regime data which has the 'Volatility' column
    df = pd.read_csv('data/regime_data.csv', index_col=0, parse_dates=True)
    vol_series = df['Volatility'].dropna()
    
    # Fit ARIMA Model (using a standard (1,1,1) configuration for financial series)
    # This will captures the momentum and mean-reversion of volatility
    model = ARIMA(vol_series, order=(1, 1, 1))
    model_fit = model.fit()
    
    # Forecasting next 5 days
    forecast = model_fit.forecast(steps=5)
    
    # Saving forecast
    forecast_df = pd.DataFrame({'Forecasted_Volatility': forecast})
    forecast_df.to_csv('data/volatility_forecast.csv')
    
    print("ARIMA Volatility Forecasting Complete.")
    print("Next 5-Day Volatility Forecast:")
    print(forecast_df)
    return forecast_df

if __name__ == "__main__":
    forecast_volatility()