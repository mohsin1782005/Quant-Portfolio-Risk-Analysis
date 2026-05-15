import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visuals():
    plt.style.use('seaborn-v0_8-whitegrid')
    os.makedirs('outputs', exist_ok=True)
    
    returns_df = pd.read_csv('data/processed_returns.csv', index_col=0, parse_dates=True)
    regime_df = pd.read_csv('data/regime_data.csv', index_col=0, parse_dates=True)
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 18), layout='constrained')
    
    # Plot 1: Portfolio Returns
    axes[0].plot(returns_df.index, returns_df['Portfolio'], color='royalblue', linewidth=0.8)
    axes[0].set_title('I. Portfolio Daily Returns', fontsize=16, fontweight='bold', pad=25)
    axes[0].set_ylabel('Returns')

    # Plot 2: Volatility & Regimes
    scatter = axes[1].scatter(regime_df.index, regime_df['Volatility'], 
                               c=regime_df['Regime'], cmap='coolwarm', s=15, alpha=0.7)
    
    axes[1].set_title('II. Market Volatility Regimes (K-Means)', fontsize=16, fontweight='bold', pad=30)
    axes[1].set_ylabel('Rolling Volatility')
    plt.colorbar(scatter, ax=axes[1], label='Regime Intensity')
    
    # Plot 3: Distribution
    sns.histplot(returns_df['Portfolio'], kde=True, ax=axes[2], color='darkslategrey', bins=60)
    axes[2].set_title('III. Return Distribution (Tail Risk Analysis)', fontsize=16, fontweight='bold', pad=30)
    axes[2].set_xlabel('Daily Return %')

    # Auto-rotating dates
    fig.autofmt_xdate()
    
    plt.savefig('outputs/portfolio_final_dashboard.png', dpi=300, bbox_inches='tight')
    print("Dashboard saved.")
    plt.show()

if __name__ == "__main__":
    generate_visuals()