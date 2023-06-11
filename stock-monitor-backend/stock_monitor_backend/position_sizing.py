import pandas as pd
from pypfopt import black_litterman
from stock_monitor_data.data import portfolio


def get_portfolio_market_prices() -> pd.DataFrame:
    for s in portfolio():
        ...


def get_weights():
    black_litterman.market_implied_risk_aversion()
