import matplotlib.pyplot as plt

def plot_pnl(pnl):
    """Plot cumulative PnL."""
    plt.figure(figsize=(10, 6))
    plt.plot(pnl.index, pnl['pnl'], label='PnL')
    plt.title('Options Strategy PnL')
    plt.xlabel('Date')
    plt.ylabel('PnL ($)')
    plt.legend()
    plt.grid()
    plt.show()