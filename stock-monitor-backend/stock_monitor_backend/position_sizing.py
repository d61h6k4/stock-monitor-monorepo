from typing import Mapping
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from pypfopt import black_litterman
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.objective_functions import L2_reg

from stock_monitor_data.data import portfolio
from stock_monitor_data.models import Stock


def get_market_prices() -> pd.Series:
    return Stock(ticker_name="SPY", period="2y", interval="1d").history["Close"]


def get_portfolio_prices() -> pd.DataFrame:
    prices = []
    for s in portfolio("2y", "1d"):
        prices.append(s.history.rename(columns={"Close": s.ticker_name})[s.ticker_name])
    return pd.concat(prices, axis=1).fillna(0.0)


def get_portfolio_market_cap() -> Mapping[str, float]:
    return {s.ticker_name: s.market_cap
            for s in portfolio("2y", "1d")}


def desired_stock_price_velocity(s: Stock) -> float:
    current_price = s.history["Close"].last(offset="1d").max()
    expected_excess = (s.expectation.price - current_price) / current_price
    time_penalty = (s.expectation.date - datetime.now(tz=timezone.utc)).days
    assert time_penalty > 0, s.ticker_name
    return expected_excess / float(time_penalty)


def get_portfolio_views() -> Mapping[str, float]:
    def _view(s: Stock) -> float:
        return 92.0 * desired_stock_price_velocity(s)  # price of a stock in 3 months

    return {s.ticker_name: _view(s)
            for s in portfolio("2y", "1d")}


def get_portfolio_view_confidences() -> pd.Series:
    def _weighted_confidence(s: Stock):
        price_velocity = desired_stock_price_velocity(s)
        price_velocity_volatility = s.history["Close"].pct_change().std()
        weight = np.ceil(price_velocity / price_velocity_volatility)

        return s.expectation.confidence / weight

    return pd.Series({s.ticker_name: _weighted_confidence(s) for s in portfolio("2y", "1d")})


def get_weights():
    cov_matrix = get_portfolio_prices().cov()
    delta = black_litterman.market_implied_risk_aversion(get_market_prices())
    bl = black_litterman.BlackLittermanModel(cov_matrix=cov_matrix,
                                             absolute_views=get_portfolio_views(),
                                             pi="market",
                                             market_caps=get_portfolio_market_cap(),
                                             omega="idzorek",
                                             view_confidences=get_portfolio_view_confidences(),
                                             risk_aversion=delta)
    bl.bl_weights(risk_aversion=delta)
    rets = bl.bl_returns()
    ef = EfficientFrontier(rets, cov_matrix)
    ef.add_objective(L2_reg)
    ef.max_sharpe()
    return ef.clean_weights(rounding=2), bl.clean_weights(rounding=2)
