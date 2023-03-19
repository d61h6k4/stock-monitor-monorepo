from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from structlog import get_logger
from typing import Mapping, Any
from stock_monitor_backend.models import Stock
from stock_monitor_backend.math import best_price_in_period, last_atr


class BotAction(str, Enum):
    """Supported action names."""
    ASR_REMINDER = "action_react_to_asr_reminder"


class CustomRasaBotMessage(BaseModel):
    name: BotAction
    entities: Mapping[str, Any]


class RasaBotMessage(BaseModel):
    custom: CustomRasaBotMessage


class Action(str, Enum):
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"


class Decision(BaseModel):
    action: Action
    explanation: str


def asr_rule(ticker: str) -> Decision:
    stock = Stock(ticker_name=ticker, period="2y", interval="1d")

    current_price = stock.history["Close"].last(offset="1D").max()
    sell_price = best_price_in_period(stock.history) - 2 * last_atr(stock.history)

    exp_msg = (f"ASR rule compares {ticker}'s current price with "
               "max price in the last 14 days minus 2 ATR. ")
    decision_action = Action.HOLD
    if current_price < sell_price:
        decision_action = Action.SELL

    exp_msg += f"Current price = {current_price}), Sell price = {sell_price}) => {decision_action}"
    return Decision(action=decision_action, explanation=exp_msg)


def create_app():
    app = FastAPI()
    logger = get_logger()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.post("/bot")
    async def bot(r: RasaBotMessage):
        match r.custom.name:
            case BotAction.ASR_REMINDER:
                logger.debug(f"{asr_rule(r.custom.entities['ticker'])=}")
            case _:
                logger.debug(r)
        return {"message": 'ok'}

    return app


def main():
    import uvicorn
    uvicorn.run(create_app())


if __name__ == "__main__":
    main()
