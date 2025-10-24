import os
from datetime import datetime

class ReportGenerator:
    def _init_(self, output_dir="outputs/reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_text_report(self, metrics: dict) -> str:
        lines = [
            f" Portfolio Report: {metrics.get('portfolio_name', 'Unnamed')}",
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Value: ${metrics.get('total_value', 0):,.2f}",
            f"Annual Return: {metrics.get('annual_return', 0):.2%}",
            f"Annual Volatility: {metrics.get('annual_volatility', 0):.2%}",
            f"Sharpe Ratio: {metrics.get('Sharpe_Ratio', 'N/A')}",
            f"Max Drawdown: {metrics.get('Max_Drawdown', 'N/A')}",
            f"VaR (95%): {metrics.get('VaR', 'N/A')}",
            f"Expected Shortfall (95%): {metrics.get('Expected_Shortfall', 'N/A')}",
        ]
        return "\n".join(lines)

    def save_report(self, metrics: dict):
        report = self.generate_text_report(metrics)
        filename = f"{metrics.get('portfolio_name', 'Unnamed').replace(' ', '_')}_report.txt"
        path = os.path.join(self.output_dir, filename)
        with open(path, "w") as f:
            f.write(report)
        print(f" Report saved to {path}")