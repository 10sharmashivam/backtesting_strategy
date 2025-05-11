# backtesting_strategy
# Options Strategy Backtester & PnL Analyzer

## Overview
A Python-based backtesting engine for options trading strategies (e.g., Iron Condor) on NIFTY 50, using historical data from yFinance. Calculates Greeks (Delta, Gamma, Theta) with QuantLib, computes performance metrics (Sharpe Ratio, Max Drawdown), and visualizes PnL curves.

## Features
- Backtests Iron Condor strategy with simulated premiums.
- Calculates option Greeks using Black-Scholes via QuantLib.
- Computes Sharpe Ratio and Max Drawdown.
- Visualizes PnL with Matplotlib.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/10sharmashivam/backtesting_strategy.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the backtest:
   ```bash
   python main.py

# Project Structure

```
/options-backtester
├── data/                 # Store historical data (optional caching)
├── src/
│   ├── strategies.py     # Iron Condor strategy logic
│   ├── backtester.py     # Backtesting engine
│   ├── greeks.py        # Greeks calculations using QuantLib
│   ├── metrics.py       # Sharpe Ratio, Max Drawdown
│   ├── visualization.py  # PnL plotting
├── tests/                # Placeholder for unit tests
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
├── main.py              # Entry point
```