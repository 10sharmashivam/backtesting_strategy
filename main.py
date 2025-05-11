import yfinance as yf
import pandas as pd
from src.strategies import iron_condor
from src.backtester import backtest
from src.metrics import sharpe_ratio, max_drawdown
from src.visualization import plot_pnl
from src.greeks import calculate_greeks

def main():
    # Fetch historical data
    nifty = yf.Ticker("^NSEI")  # NIFTY 50 index
    data = nifty.history(period="1y", interval="1d")

    # Run backtest
    pnl = backtest(data, iron_condor, capital=100000)

    # Calculate metrics
    returns = pnl['pnl'].pct_change().dropna()
    sharpe = sharpe_ratio(returns)
    mdd = max_drawdown(pnl['pnl'])
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {mdd:.2%}")

    # Calculate Greeks for a sample option
    spot = data['Close'][-1]
    greeks = calculate_greeks(spot=spot, strike=spot + 100, option_type="call")
    print("Greeks:", greeks)

    # Plot PnL
    plot_pnl(pnl)

if __name__ == "__main__":
    main()