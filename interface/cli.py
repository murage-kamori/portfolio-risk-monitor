import sys
import os
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)
    
import argparse
from portfolio_monitor import PortfolioManager
from risk_visualizer import RiskVisualizer
from risk_calculator import RiskCalculator


def main():
    # Set up arguments
    parser = argparse.ArgumentParser(description="Run portfolio risk analysis from the terminal.")
    parser.add_argument("--portfolio", required=True, help="Path to the portfolio CSV file.")
    parser.add_argument("--name", required=True, help="Name of the portfolio.")
    parser.add_argument("--benchmark", help="Path to the benchmark CSV file (optional).")
    parser.add_argument("--window", type=int, default=21, help="Rolling window size (default: 21).")
    parser.add_argument("--configdir", default="config", help="Directory to save config (default: config).")
    parser.add_argument("--save-config", action="store_true", help="Save portfolio config to JSON")
    parser.add_argument("--export-report", action="store_true", help="Export risk report to file")

    args = parser.parse_args()

    # Initialize portfolio manager
    manager = PortfolioManager(config_dir=args.configdir)

    # Load portfolio
    portfolio = manager.load_portfolio_from_csv(args.portfolio, args.name)

    # Save config if requested
    if args.save_config:
        manager.save_portfolio_config(portfolio)

    # Load benchmark if provided
    if args.benchmark:
        benchmark_returns = manager.load_benchmark_returns(args.benchmark)
        manager.benchmarkreturns = benchmarkreturns

    # Plot volatility comparison
    manager.compare_volatility(window=args.window)


    # Calculate portfolio returns
    returnsdf = manager.getportfolio_returns()
    portfolio_returns = manager.get_portfolio_returns(args.name)
     # weighted sum assumed
    
    #call
    visualizer = RiskVisualizer(portfolio_returns, ticker="Tech Portfolio")
    visualizer.plot_comparison(benchmark_returns)

    # Run risk analysis
    rc = RiskCalculator(portfolio_returns)
    metrics = rc.calculateallmetrics()

    # Print metrics
    print(f"\n Risk Metrics for {args.name}")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    # Print benchmark Sharpe ratio if available
    if args.benchmark:
        benchmarksharpe = RiskCalculator(manager.benchmarkreturns.sum(axis=1)).calculatesharperatio()
        print(f"\nBenchmark Sharpe Ratio: {benchmarksharpe:.3f}")

if __name__ == "__main__":
    main()

  parser.add_argument("--export-report", action="store_true", help="Save text report to outputs/reports")
if args.export_report:
    from report_generator import ReportGenerator
    ReportGenerator() .save_report
    
    
    