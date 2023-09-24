"""Collections of rules."""

from enum import Enum

from pydantic import BaseModel


class Action(str, Enum):
    """Enumerate possible of actions of rules."""

    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"

    @staticmethod
    def from_string(s: str) -> "Action":
        match s:
            case "buy":
                return Action.BUY
            case "hold":
                return Action.HOLD
            case "sell":
                return Action.SELL
            case _:
                raise ValueError(s)


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


def macd_rule(
    ticker: str, current_price: float, macd_value: float, signal_value: float
) -> Decision:
    """MACD rule.

    https://www.investopedia.com/terms/m/macd.asp
    """

    rule = Rule(
        name="MACD",
        description="Moving average convergence/divergence (MACD, or MAC-D) is a "
        "trend-following momentum indicator that shows the relationship "
        "between two exponential moving averages (EMAs) of a security`s price. "
        "The MACD line is calculated by subtracting the 26-period EMA from "
        "the 12-period EMA. The result of that calculation is the MACD line. "
        "A nine-day EMA of the MACD line is called the signal line, which is "
        "then plotted on top of the MACD line, which can function as a trigger "
        "for buy or sell signals.",
    )

    decision_action = Action.BUY
    if macd_value <= signal_value:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f}."
    return Decision(
        ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg
    )


def rsi_rule(ticker: str, current_price: float, rsi_value: float) -> Decision:
    """RSI rule."""

    rule = Rule(
        name="RSI",
        description="The relative strength index (RSI) is a momentum indicator used in "
        "technical analysis. RSI measures the speed and magnitude of a security's "
        "recent price changes to evaluate overvalued or undervalued conditions in "
        "the price of that security. RSI < 30 -> OverSold => Buy. RSI > 70 -> OverBought => Sell.",
    )

    decision_action = Action.HOLD
    if rsi_value < 30:
        decision_action = Action.BUY
    elif rsi_value > 70:
        decision_action = Action.SELL

    exp_msg = f"Current price is {current_price:,.2f}, RSI value is {rsi_value:,.1f}."
    return Decision(
        ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg
    )


def adx_rule(
    ticker: str,
    current_price: float,
    positive_di_value: float,
    negative_di_value: float,
    adx_value: float,
) -> Decision:
    """ADX rule."""

    rule = Rule(
        name="ADX",
        description="The average directional index (ADX) is a technical analysis "
        "indicator used by some traders to determine the strength of a trend."
        "The ADX identifies a strong trend when the ADX is over 25 and a weak "
        "trend when the ADX is below 20. Crossovers of the -DI and +DI lines can "
        "be used to generate trade signals. For example, if the +DI line crosses "
        "above the -DI line and the ADX is above 20, or ideally above 25, then "
        "that is a potential signal to buy. On the other hand, if the -DI crosses "
        "above the +DI, and the ADX is above 20 or 25, then that is an opportunity "
        "to enter a potential short trade.",
    )

    decision_action = Action.HOLD
    if adx_value > 25:
        decision_action = (
            Action.BUY if positive_di_value > negative_di_value else Action.SELL
        )

    exp_msg = f"Current price is {current_price:,.2f}, ADX = {adx_value:,.1f}, +DI = {positive_di_value:,.1f}, -DI = {negative_di_value:,.1f}."
    return Decision(
        ticker=ticker, rule=rule, action=decision_action, explanation=exp_msg
    )
