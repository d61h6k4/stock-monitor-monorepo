from enum import Enum
from pydantic import BaseModel
from stock_monitor_backend.math import best_price_in_period, last_atr
from stock_monitor_backend.models import Stock


class Action(str, Enum):
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"


class Rule(BaseModel):
    name: str
    description: str


class Decision(BaseModel):
    ticker: str
    rule: Rule
    action: Action
    explanation: str


def asr_rule(ticker: str) -> Decision:
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    sell_price = best_price_in_period(stock.history) - 2 * last_atr(stock.history)

    rule = Rule(name="ASR",
                description=f"ASR rule compares ${ticker}'s current price with "
                            "max price in the last 14 days minus 2 ATR")

    decision_action = Action.HOLD
    if current_price < sell_price:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f} and sell price is {sell_price:,.2f} \U000027A1 {decision_action}"
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)
