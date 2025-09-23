import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.portfolio_monitor import Portfolio, PortfolioManager

# ─── Manual Portfolio Test ─────────────────────────────────────────────
print("\n=== Manual Portfolio Test ===")
manual_portfolio = Portfolio(name="Test Portfolio")
manual_portfolio.add_holding("AAPL", 100)
manual_portfolio.add_holding("GOOGL", 50)
manual_portfolio.remove_holding("AAPL")
manual_portfolio.portfolio_summary()

# ─── CSV Portfolio Test ────────────────────────────────────────────────
print("\n=== CSV Portfolio Test ===")
manager = PortfolioManager()
csv_portfolio = manager.load_portfolio_from_csv("sample_portfolio.csv", "Demo Portfolio")
csv_portfolio.portfolio_summary()

csv_portfolio.add_holding("TSLA", 25)
csv_portfolio.remove_holding("BAC")
csv_portfolio.portfolio_summary()

manager.save_portfolio_config(csv_portfolio)

from src.risk_calculator import RiskCalculator

# ─── Risk Metrics 
print("\n=== Risk Metrics ===")
returns = manager.load_returns_from_csv("sample_returns.csv")
rc = RiskCalculator(returns)

print("VaR (95%):", rc.calculate_var())
print("Volatility:", rc.calculate_volatility())
print("Max Drawdown:", rc.calculate_max_drawdown())

from src.risk_visualizer import RiskVisualizer

#Risk Charts
viz = RiskVisualizer(returns)
viz.plot_drawdown()
viz.plot_return_distribution()
viz.plot_drawdown(save_path="outputs/drawdown.png")
viz.plot_return_distribution(save_path="outputs/return_distribution.png")


print("Sharpe Ratio:", rc.calculate_sharpe_ratio())
viz.plot_rolling_volatility(window=20)


# ─── Benchmark Comparison 
benchmark_returns = manager.load_benchmark_returns("benchmark_spy.csv")
benchmark_rc = RiskCalculator(benchmark_returns)

print("\n=== Benchmark (SPY) Metrics ===")
print("VaR (95%):", benchmark_rc.calculate_var())
print("Volatility:", benchmark_rc.calculate_volatility())
print("Max Drawdown:", benchmark_rc.calculate_max_drawdown())
print("Sharpe Ratio:", benchmark_rc.calculate_sharpe_ratio())

viz.plot_comparison(benchmark_returns)