import argparse
from portfolio_monitor.py import PortfolioManager
from risk_visualizer import plot_comparison

def main():
    #set up arguments
    parser = argparse.ArgumentParser(description="Run portfolio risk analysis from the terminal.")
    parser.add_argument("--portfolio", required=True, help="Path to the portfolio csv file.")
    parser.add_argument("--name", required=True, help="Name of the portfolio.")
    parser.add_argument("--benchmark", help="Path to the benchmark csv file(Optional).")
    parser.add_argument("--window", type=int, default=21, help="Rolling window size (default: 21).")
    parser.add_argument("--config_dir", default="config", help="Directory to save config(default: config).")
    parser.add_argument("--save-config", action="store_true", help="Save portfolio config to JSON")
    
    args = parser.parse_args()
    
    #initialize portfolio manager
    manager = PortfolioManager(data_dir="data", config_dir=args.config_dir)
    
    #load portfolio from csv
    portfolio = manager.load_portfolio_fromcsv(args.portfolio,args.name)
    
    #load benchmark if provided
    if args.benchmark:
        benchmark_returns = manager.local_benchmark_returns(args.benchmark)
        manager.benchmark_returns = benchmark_returns
        
    #plot volatility comparison
    plot_comparison(manager.compare_volatility(window=args.window))
    
    #print sharpe ratio
    print(f"\nSharpe Ratio for {args.name}: {portfolio.calculate_sharpe_ratio():. 3f}")
    
    if args.benchmark:
        print(f"Sharpe Ratio for Benchmark: {manager_benchmark_returns.calculate_sharpe_ratio():.3f}")
        
if__name__ == "__main__"
main()        

if args.save_config:
    manager.save_config(args.name, args.portfolio)