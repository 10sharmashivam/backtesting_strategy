import QuantLib as ql
from datetime import datetime

def calculate_greeks(spot, strike, expiry_days=30, vol=0.2, r=0.05, option_type="call"):
    """
    Calculate Delta, Gamma, Theta for an option using Black-Scholes.
    :param spot: Current price
    :param strike: Strike price
    :param expiry_days: Days to expiry
    :param vol: Implied volatility
    :param r: Risk-free rate
    :param option_type: 'call' or 'put'
    :return: Dictionary of Greeks
    """
    today = ql.Date(datetime.today().day, datetime.today().month, datetime.today().year)
    expiry_date = today + expiry_days
    ql.Settings.instance().evaluationDate = today

    option = ql.EuropeanOption(
        ql.PlainVanillaPayoff(ql.Option.Call if option_type == "call" else ql.Option.Put, strike),
        ql.EuropeanExercise(expiry_date)
    )
    process = ql.BlackScholesProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        ql.YieldTermStructureHandle(ql.FlatForward(today, r, ql.Actual365Fixed())),
        ql.BlackVolTermStructureHandle(ql.BlackConstantVol(today, ql.NullCalendar(), vol, ql.Actual365Fixed()))
    )
    option.setPricingEngine(ql.AnalyticEuropeanEngine(process))

    return {
        "delta": option.delta(),
        "gamma": option.gamma(),
        "theta": option.theta()
    }