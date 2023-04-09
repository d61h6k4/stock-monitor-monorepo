"""Collections of rules."""

from enum import Enum

from pydantic import BaseModel

from stock_monitor_backend.math import best_price_in_period, last_atr, moving_average_distance
from stock_monitor_backend.models import Stock


class Action(str, Enum):
    """Enumerate possible of actions of rules."""
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"


class Rule(BaseModel):
    """Rule object."""
    name: str
    description: str


class Decision(BaseModel):
    """Decision object."""
    ticker: str
    rule: Rule
    action: Action
    explanation: str


def asr_rule(ticker: str) -> Decision:
    """ASR rule."""
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    sell_price = best_price_in_period(stock.history) - 2 * last_atr(stock.history)

    rule = Rule(name="ASR",
                description=f"ASR rule compares ${ticker}'s current price with "
                            "max price in the last 14 days minus 2 ATR")

    decision_action = Action.HOLD
    if current_price < sell_price:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f} and sell price is {sell_price:,.2f}"
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)


def mad_rule(ticker: str) -> Decision:
    """MAD rule.

    Moving average distance 21/50.
    """
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")
    current_price = stock.history["Close"].last(offset="1D").max()
    mad = moving_average_distance(stock.history, 21, 50)

    rule = Rule(name="MAD",
                description="MAD rule takes the moving average price of the last 21 days "
                            "over the last 50 days and compares with threshold (1.05 and 0.95)")

    decision_action = Action.HOLD
    if mad > 1.05:
        decision_action = Action.BUY
    elif mad < 0.95:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f} and MAD is {mad:,.2f}."
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)
