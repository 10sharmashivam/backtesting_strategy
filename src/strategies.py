import pandas as pd

def iron_condor(data, strike_spread=100, premium=1000):
    """
    Simulate an Iron Condor: Sell call/put spreads, collect premium.
    :param data: DataFrame with 'Close' prices
    :param strike_spread: Distance between strikes (simplified)
    :param premium: Fixed premium for simplicity (in reality, calculate via Black-Scholes)
    :return: List of trades
    """
    trades = []
    for date, row in data.iterrows():
        spot = row['Close']
        # Simplified: Assume selling call/put spreads at fixed premium
        trade = {
            'date': date,
            'spot': spot,
            'strike_call_sell': spot + strike_spread,
            'strike_call_buy': spot + strike_spread + 50,
            'strike_put_sell': spot - strike_spread,
            'strike_put_buy': spot - strike_spread - 50,
            'premium': premium,  # Net premium received
            'status': 'open'
        }
        trades.append(trade)
    return trades