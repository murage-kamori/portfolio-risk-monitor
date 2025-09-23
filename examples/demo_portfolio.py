import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.portfolio_monitor import Portfolio
portfolio = Portfolio(name="Test Portfolio")
portfolio.add_holding("AAPL", 100)
portfolio.add_holding("GOOGL", 50)
portfolio.remove_holding("AAPL")
portfolio.portfolio_summary()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from src.portfolio_monitor import PortfolioManager

# Initialize manager
manager = PortfolioManager()

# Load portfolio from CSV
portfolio = manager.load_portfolio_from_csv("sample_portfolio.csv", "Demo Portfolio")

# Show initial summary
portfolio.portfolio_summary()

# Add a new holding
portfolio.add_holding("TSLA", 25)

# Remove a holding
portfolio.remove_holding("BAC")

# Show updated summary
portfolio.portfolio_summary()

# Save config to JSON
manager.save_portfolio_config(portfolio)