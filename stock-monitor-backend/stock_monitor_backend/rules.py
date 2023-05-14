"""Collections of rules."""

from enum import Enum

from pydantic import BaseModel

from stock_monitor_backend.math import best_price_in_period, last_atr, moving_average_distance, macd, rsi, adx
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


def macd_rule(ticker: str) -> Decision:
    """MACD rule.

    https://www.investopedia.com/terms/m/macd.asp
    """
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    macd_line = macd(stock.history)
    signal_line = macd_line.ewm(alpha=1. / 9.).mean()

    macd_value = macd_line.last(offset="1d").max()
    signal_value = signal_line.last(offset="1d").max()

    rule = Rule(name="MACD",
                description="Moving average convergence/divergence (MACD, or MAC-D) is a "
                            "trend-following momentum indicator that shows the relationship "
                            "between two exponential moving averages (EMAs) of a security’s price. "
                            "The MACD line is calculated by subtracting the 26-period EMA from "
                            "the 12-period EMA. The result of that calculation is the MACD line. "
                            "A nine-day EMA of the MACD line is called the signal line, which is "
                            "then plotted on top of the MACD line, which can function as a trigger "
                            "for buy or sell signals.")

    decision_action = Action.BUY
    if macd_value <= signal_value:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f}."
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)


def rsi_rule(ticker: str) -> Decision:
    """RSI rule.
    """
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    rsi_line = rsi(stock.history)
    rsi_value = rsi_line.last(offset="1d").max()

    rule = Rule(name="RSI",
                description="The relative strength index (RSI) is a momentum indicator used in "
                            "technical analysis. RSI measures the speed and magnitude of a security's "
                            "recent price changes to evaluate overvalued or undervalued conditions in "
                            "the price of that security. RSI < 30 -> OverSold => Buy. RSI > 70 -> OverBought => Sell.")

    decision_action = Action.HOLD
    if rsi_value < 30:
        decision_action = Action.BUY
    elif rsi_value > 70:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f}, RSI value is {rsi_value:,.1f}."
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)


def adx_rule(ticker: str) -> Decision:
    """ADX rule.
    """
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    adx_data = adx(stock.history)

    positive_di_value = adx_data["+di"].last(offset="1d").max()
    negative_di_value = adx_data["-di"].last(offset="1d").max()
    adx_value = adx_data["adx"].last(offset="1d").max()

    rule = Rule(name="ADX",
                description="The average directional index (ADX) is a technical analysis "
                            "indicator used by some traders to determine the strength of a trend."
                            "The ADX identifies a strong trend when the ADX is over 25 and a weak "
                            "trend when the ADX is below 20. Crossovers of the -DI and +DI lines can "
                            "be used to generate trade signals. For example, if the +DI line crosses "
                            "above the -DI line and the ADX is above 20, or ideally above 25, then "
                            "that is a potential signal to buy. On the other hand, if the -DI crosses "
                            "above the +DI, and the ADX is above 20 or 25, then that is an opportunity "
                            "to enter a potential short trade.")

    decision_action = Action.HOLD
    if adx_value > 25:
        if positive_di_value > negative_di_value:
            decision_action = Action.BUY
        else:
            decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f}, ADX = {adx_value:,.1f}, +DI = {positive_di_value:,.1f}, -DI = {negative_di_value:,.1f}."
    return Decision(ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg)
