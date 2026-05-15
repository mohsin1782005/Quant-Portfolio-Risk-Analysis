import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import os

def detect_regimes():
    # Load returns here
    returns = pd.read_csv('data/processed_returns.csv', index_col=0, parse_dates=True)
    port_returns = returns[['Portfolio']].copy()
    
    # Feature Engineering: 21-day Rolling Volatility
    port_returns['Volatility'] = port_returns['Portfolio'].rolling(window=21).std()
    port_returns = port_returns.dropna()
    
    # K-Means Clustering (3 Regimes: Low, Mid, High)
    X = port_returns[['Volatility']].values
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    port_returns['Regime'] = kmeans.fit_predict(X)
    
    # Sorting regimes by volatility level so 0=Low, 1=Mid, 2=High
    idx = np.argsort(kmeans.cluster_centers_.sum(axis=1))
    lut = dict(zip(idx, [0, 1, 2]))
    port_returns['Regime'] = port_returns['Regime'].map(lut)
    
    # Saving
    port_returns.to_csv('data/regime_data.csv')
    print("Regime Detection Complete. Market segmented into 3 Volatility States.")
    print(port_returns['Regime'].value_counts().sort_index())
    return port_returns

if __name__ == "__main__":
    detect_regimes()