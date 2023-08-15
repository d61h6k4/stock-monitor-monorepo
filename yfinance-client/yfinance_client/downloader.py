from yfinance import Ticker
from typing import NamedTuple


class TickerPrice(NamedTuple):
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    dividends: float
    kind: str = "TICKER_PRICE"


def get_ticker_events(symbol: str):
    """Returns events of the ticker.

    Args:
        symbol - the ticker's symbol
        price_date - the date of the price
        is_past - when True, there is no news or info as event generated

    Returns:
        events.
    """
    yield from get_ticker_history_events(symbol=symbol, period="1d")


def get_ticker_history_events(symbol: str, period: str = "max"):
    """Returns events of the ticker.

    Args:
        symbol - the ticker's symbol

    Returns:
        events.
    """
    ticker = Ticker(symbol)

    for date, values in ticker.history(period=period, interval="1d").iterrows():
        yield TickerPrice(
            symbol=symbol,
            date=date.to_pydatetime().isoformat(),
            open=values["Open"],
            high=values["High"],
            low=values["Low"],
            close=values["Close"],
            volume=values["Volume"],
            dividends=values["Dividends"],
        )
