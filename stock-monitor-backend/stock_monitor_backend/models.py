"""Collection of the data models."""

from collections.abc import Mapping
from pathlib import Path

from pandas import DataFrame
from pydantic import BaseModel, validator
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from yfinance import Ticker


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """Caches requests session and limits requests num."""


session = CachedLimiterSession(
    expire_after=3600,
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache(str(Path(__file__).parent.parent.resolve() / "yfinance.cache")),
)


class Stock(BaseModel):
    """Representation of the stock data model."""
    ticker_name: str
    period: str
    interval: str
    history: DataFrame = DataFrame()

    class Config:
        """Allow DataFrame."""
        arbitrary_types_allowed = True

    @validator("period")
    def is_valid_period_value(cls: "Stock", period: str) -> str:
        """Check the period value from predetermined set."""
        valid_periods = {"1d", "5d", "1mo", "3mo", "6mo",
                         "1y", "2y", "5y", "10y", "ytd", "max"}
        if period not in valid_periods:
            msg = (f"Given period {period} is not valid. "
                   f"Valid periods: {','.join(valid_periods)}")
            raise ValueError(msg)

        return period

    @validator("interval")
    def is_valid_interval_value(cls: "Stock", interval: str) -> str:
        """Checks the interval value from predetermined set."""
        valid_intervals = {"1m", "2m", "5m", "15m", "30m", "60m",
                           "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"}
        if interval not in valid_intervals:
            msg = (f"Given interval {interval} is not valid. "
                   f"Valid intervals: {','.join(valid_intervals)}")
            raise ValueError(msg)

        return interval

    @validator("history", always=True)
    def download_history(cls: "Stock",
                         history: DataFrame,
                         values: Mapping[str, str]) -> DataFrame:
        """Downloads history data."""
        assert history.empty

        ticker = Ticker(values["ticker_name"], session=session)
        return ticker.history(period=values["period"], interval=values["interval"])
