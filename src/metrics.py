import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.05, periods_per_year=252):
    """Calculate annualized Sharpe Ratio."""
    mean_return = returns.mean() * periods_per_year
    std_return = returns.std() * np.sqrt(periods_per_year)
    return (mean_return - risk_free_rate) / std_return

def max_drawdown(pnl):
    """Calculate maximum drawdown."""
    cumulative = pnl.cumsum()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()