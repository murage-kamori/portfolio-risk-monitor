from datetime import datetime

class Portfolio:
    def __init__(self, name, holdings=None, benchmark="SPY"):
        """
        Initialize a portfolio with a name, holdings, and benchmark.
        holdings: dict of {symbol: quantity}
        benchmark: default comparison index (e.g., SPY)
        """
        self.name = name
        self.holdings = holdings if holdings else {}
        self.benchmark = benchmark
        self.created_date = datetime.now()
        self.last_updated = datetime.now()

    def add_holding(self, symbol, quantity):
        """
        Add or update a holding in the portfolio.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.holdings[symbol] = quantity
        self.last_updated = datetime.now()

    def remove_holding(self, symbol):
        """
        Remove a holding from the portfolio.
        """
        removed = self.holdings.pop(symbol, None)
        self.last_updated = datetime.now()
        return removed

    def get_symbols(self):
        """
        Return a list of all symbols in the portfolio.
        """
        return list(self.holdings.keys())

    def get_total_positions(self):
        """
        Return the number of holdings.
        """
        return len(self.holdings)

    def portfolio_summary(self):
        """
        Print a summary of the portfolio.
        """
        print(f"\nPORTFOLIO SUMMARY: {self.name}")
        print("=" * 50)
        print(f"Benchmark: {self.benchmark}")
        print(f"Created: {self.created_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Last Updated: {self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Positions: {self.get_total_positions()}")
        print("Holdings:")
        for symbol, qty in self.holdings.items():
            print(f"  {symbol}: {qty} shares")
        print("=" * 50)
        
        
        import os
import json
import pandas as pd

class PortfolioManager:
    def __init__(self, config_dir="config", data_dir="data", output_dir="outputs"):
        self.config_dir = config_dir
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.ensure_directories()

    def ensure_directories(self):
        """
        Create necessary folders if they don't exist.
        """
        for folder in [self.config_dir, self.data_dir, self.output_dir,
                       os.path.join(self.output_dir, "reports"),
                       os.path.join(self.output_dir, "charts")]:
            os.makedirs(folder, exist_ok=True)

    def load_portfolio_from_csv(self, filename, portfolio_name, benchmark="SPY"):
        """
        Load portfolio holdings from a CSV file.
        Returns a Portfolio object.
        """
        filepath = os.path.join(self.data_dir, filename)
        df = pd.read_csv(filepath)

        holdings = {}
        for _, row in df.iterrows():
            symbol = row["Symbol"]
            quantity = int(row["Quantity"])
            holdings[symbol] = quantity

        return Portfolio(name=portfolio_name, holdings=holdings, benchmark=benchmark)

    def save_portfolio_config(self, portfolio):
        """
        Save portfolio metadata to a JSON config file.
        """
        config = {
            "name": portfolio.name,
            "benchmark": portfolio.benchmark,
            "created_date": portfolio.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "last_updated": portfolio.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
            "holdings": portfolio.holdings
        }

        filepath = os.path.join(self.config_dir, "portfolio_config.json")
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)