import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class RiskVisualizer:
    def __init__(self, returns,ticker="Portfolio"):
        self.returns = returns.dropna()
        self.ticker = ticker

    def plot_drawdown(self, save_path=None):
        """
        Plot cumulative drawdown over time.
        """
        cumulative = (1 + self.returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak

        plt.figure(figsize=(10, 4))
        drawdown.plot(color='red')
        plt.title(f"{{self.ticker}} Drawdown Over Time")
        plt.ylabel('Drawdown')
        plt.xlabel('Date')
        plt.grid(True)
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
            
            
    def plot_return_distribution(self,bins=30, save_path=None):
     """
     Histogram of daily returns.
     """
     plt.figure(figsize=(8, 4))
     plt.hist(self.returns, bins=bins, color='steelblue', edgecolor='black')
     plt.title(f"{self.ticker} - Return Distribution")
     plt.xlabel('Daily Return')
     plt.ylabel('Frequency')
     plt.grid(True)
     if save_path:
        plt.savefig(save_path)
     else:
        plt.show()
        
        
    def calculate_rolling_volatility(self, window=20):
     """
     Rolling volatility over a specified window (default: 20 days).
     """
     rolling_vol = self.returns.rolling(window).std() * np.sqrt(252)
     return rolling_vol


    def calculate_sharpe_ratio(self, risk_free_rate=0.01):
     """
     Sharpe ratio using mean excess return over volatility.
     Assumes daily returns and annualizes.
     """
     excess_return = self.returns.mean() * 252 - risk_free_rate
     volatility = self.returns.std() * np.sqrt(252)
     sharpe = excess_return / volatility if volatility != 0 else np.nan
     return round(sharpe, 4)

    def plot_rolling_volatility(self, window=20, save_path=None):
     """
     Plot rolling volatility over time.
     """
     import matplotlib.pyplot as plt
     import numpy as np
     
     rolling_vol = self.returns.rolling(window).std() * np.sqrt(252)

     plt.figure(figsize=(10, 4))
     rolling_vol.plot(title=f'{window}-Day Rolling Volatility', color='purple')
     plt.title(f"{self.ticker} - {window}-Day Rolling Volatility")
     plt.xlabel('Date')
     plt.ylabel('Annualized Volatility')
     plt.grid(True)
     if save_path:
        plt.savefig(save_path)
     else:
        plt.show()
        
        
    def plot_comparison(self, benchmark_returns, save_path=None):
     """
     Compare cumulative returns of portfolio vs benchmark.
     """
     portfolio_cum = (1 + self.returns).cumprod()
     benchmark_cum = (1 + benchmark_returns.dropna()).cumprod()

     plt.figure(figsize=(10, 4))
     portfolio_cum.plot(label='Portfolio', color='blue')
     benchmark_cum.plot(label='Benchmark', color='green')
     plt.title(f"{self.ticker} vs Benchmark - Cumulative Returns")
     plt.xlabel('Date')
     plt.ylabel('Growth of $1')
     plt.legend()
     plt.grid(True)
     if save_path:
        plt.savefig(save_path)
     else:
        plt.show()


    # The following method is a duplicate and should be removed to avoid confusion and errors.


    