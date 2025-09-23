import numpy as np
import pandas as pd

class RiskCalculator:
    def __init__(self, returns: pd.Series):
        self.returns = returns.dropna()

    def calculate_var(self, confidence_level=0.95):
        """
        Historical Value at Risk (VaR) using percentile method.
        """
        var = np.percentile(self.returns, (1 - confidence_level) * 100)
        return round(var, 4)

    def calculate_volatility(self):
        """
        Annualized volatility based on daily returns.
        """
        daily_vol = self.returns.std()
        annual_vol = daily_vol * np.sqrt(252)
        return round(annual_vol, 4)

    def calculate_max_drawdown(self):
        """
        Maximum drawdown from peak to trough.
        """
        cumulative = (1 + self.returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        max_dd = drawdown.min()
        return round(max_dd, 4)
    
    def calculate_sharpe_ratio(self, risk_free_rate=0.01):
     """
     Sharpe ratio using mean excess return over volatility.
     Assumes daily returns and annualizes.
     """
     excess_return = self.returns.mean() * 252 - risk_free_rate
     volatility = self.returns.std() * np.sqrt(252)
     sharpe = excess_return / volatility if volatility != 0 else np.nan
     return round(sharpe, 4)