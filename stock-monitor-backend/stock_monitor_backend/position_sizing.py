import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timezone
from pypfopt import black_litterman
from pypfopt.efficient_frontier import EfficientFrontier
from stock_monitor_data.data import portfolio
from stock_monitor_data.models import Stock
from typing import Mapping


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


def get_portfolio_views() -> Mapping[str, float]:
    def _view(s: Stock) -> float:
        current_price = s.history["Close"].last(offset="1d").max()
        expected_excess = (s.expectation.price - current_price) / current_price
        time_penalty = (s.expectation.date - datetime.now(tz=timezone.utc)).days / 66.

        return expected_excess / time_penalty

    return {s.ticker_name: _view(s)
            for s in portfolio("2y", "1d")}


def get_portfolio_view_confidences() -> Mapping[str, float]:
    confidences = pd.Series({s.ticker_name: s.expectation.confidence for s in portfolio("2y", "1d")})
    return confidences


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
    return bl.clean_weights(rounding=2)
