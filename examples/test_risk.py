import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.risk_calculator import RiskCalculator

# Simulated daily returns
returns = pd.Series([0.01, -0.02, 0.015, -0.005, 0.02, -0.03, 0.01, 0.005, -0.01, 0.02])

rc = RiskCalculator(returns)

print("VaR (95%):", rc.calculate_var())
print("Volatility:", rc.calculate_volatility())
print("Max Drawdown:", rc.calculate_max_drawdown())