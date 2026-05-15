import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def run_forecasting(ticker_name):
    # Loading raw data for prices
    df = pd.read_csv('data/raw_data.csv', index_col=0, parse_dates=True)
    
    # Selecting one stock and creating "Lag" features (using past 5 days to predict today)
    data = df[[ticker_name]].copy()
    for i in range(1, 6):
        data[f'Lag_{i}'] = data[ticker_name].shift(i)
    
    data = data.dropna()
    
    # Features (X) and Target (y)
    X = data[[f'Lag_{i}' for i in range(1, 6)]]
    y = data[ticker_name]
    
    # Spliting data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Training Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Prediction
    prediction = model.predict(X_test[-1:])
    print(f"ML Prediction for next {ticker_name} price: {prediction[0]:.2f}")
    return prediction[0]

if __name__ == "__main__":
    # Testing on Reliance
    run_forecasting('RELIANCE.NS')