import pandas as pd

def backtest(data, strategy, capital=100000):
    """
    Backtest an options strategy.
    :param data: DataFrame with historical prices
    :param strategy: Function defining the strategy (e.g., iron_condor)
    :param capital: Initial capital
    :return: DataFrame with PnL
    """
    trades = strategy(data)
    portfolio = {"cash": capital, "positions": trades}
    pnl = []

    for i, trade in enumerate(trades):
        # Simplified: Assume trades close at next timestep with premium as profit
        date = trade['date']
        profit = trade['premium']  # In reality, calculate based on price movement
        portfolio['cash'] += profit
        pnl.append({'date': date, 'pnl': portfolio['cash'] - capital})

    return pd.DataFrame(pnl).set_index('date')