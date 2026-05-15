import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def classify_risk():
    # Loading the regime data i have created
    df = pd.read_csv('data/regime_data.csv', index_col=0, parse_dates=True)
    
    # Feature Engineering: Using past 3 days of volatility to predict the Regime
    df['Vol_Lag1'] = df['Volatility'].shift(1)
    df['Vol_Lag2'] = df['Volatility'].shift(2)
    df['Vol_Lag3'] = df['Volatility'].shift(3)
    
    df = df.dropna()
    
    # Features (X) and Target (y is the Regime: 0, 1, or 2)
    X = df[['Vol_Lag1', 'Vol_Lag2', 'Vol_Lag3']]
    y = df['Regime']
    
    # Spliting Data (Walk-forward style: no shuffle)
    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    # Training Random Forest 
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluating
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    
    print("Machine Learning Risk Classification Complete.")
    print("Classification Report:\n", report)
    
    # Savingg the model's accuracy
    with open('data/ml_report.txt', 'w') as f:
        f.write(report)
    return clf

if __name__ == "__main__":
    classify_risk()