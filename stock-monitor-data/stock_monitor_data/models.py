"""Collection of the data models."""
import io
import logging
import tempfile
import time
from typing import Any
import zipfile
from collections.abc import Mapping, Sequence
from datetime import datetime
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from pydantic import BaseModel, field_validator
from requests import Session
from requests.exceptions import HTTPError
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from yfinance import Ticker
from pyrate_limiter import Duration, RequestRate, Limiter

logger = logging.getLogger(__name__)


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """Caches requests session and limits requests num."""


session = CachedLimiterSession(
    expire_after=3600,
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("cache/yfinance.cache"),
)

slow_session = CachedLimiterSession(
    limiter=Limiter(
        RequestRate(2, Duration.SECOND * 5)
    ),  # max 2 requests per 5 seconds
    expire_after=30 * 24 * 3600,
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("cache/yfinance.slow.cache"),
)

cot_session = CachedLimiterSession(
    expire_after=24 * 3600,
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("cache/cot.cache"),
)


class Expectation(BaseModel):
    price: float
    date: datetime
    confidence: float = 1.0


class Stock(BaseModel):
    """Representation of the stock data model."""

    ticker_name: str
    period: str
    interval: str
    expectation: Expectation | None = None
    description: str = ""

    @field_validator("period")
    def is_valid_period_value(cls: "Stock", period: str) -> str:
        """Check the period value from predetermined set."""
        valid_periods = {
            "1d",
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "2y",
            "5y",
            "10y",
            "ytd",
            "max",
        }
        if period not in valid_periods:
            msg = (
                f"Given period {period} is not valid. "
                f"Valid periods: {','.join(valid_periods)}"
            )
            raise ValueError(msg)

        return period

    @field_validator("interval")
    def is_valid_interval_value(cls: "Stock", interval: str) -> str:
        """Checks the interval value from predetermined set."""
        valid_intervals = {
            "1m",
            "2m",
            "5m",
            "15m",
            "30m",
            "60m",
            "90m",
            "1h",
            "1d",
            "5d",
            "1wk",
            "1mo",
            "3mo",
        }
        if interval not in valid_intervals:
            msg = (
                f"Given interval {interval} is not valid. "
                f"Valid intervals: {','.join(valid_intervals)}"
            )
            raise ValueError(msg)

        return interval

    @property
    def history(self) -> DataFrame:
        """Downloads history data."""
        history = self.__dict__.get("history")
        if history is None:
            logger.debug("Loading history data for %s", self.ticker_name)
            ticker = Ticker(self.ticker_name, session=session)
            try:
                history = ticker.history(period=self.period, interval=self.interval)
            except HTTPError as e:
                msg = f"Ticker {self.ticker_name} doesn't exist."
                raise ValueError(msg) from e

            self.__dict__["history"] = history
        return history

    @history.setter
    def history(self, df: DataFrame):
        self.__dict__["history"] = df

    @property
    def info(self) -> Mapping[str, Any]:
        info = self.__dict__.get("info")
        if info is None:
            try:
                info = Ticker(self.ticker_name, session=slow_session).get_info()
            except HTTPError as e:
                logger.exception(f"Ticker {self.ticker_name} doesn't exist. {e!r}")
                time.sleep(1)

                info = {}
            self.__dict__["info"] = info

        return info

    @property
    def business_summary(self) -> str:
        """Extract business summary."""
        return self.info.get("longBusinessSummary", "")

    @property
    def market_cap(self) -> float:
        """Extract market cap."""
        return self.info.get("marketCap", 1.0)

    @property
    def industry(self) -> str:
        return self.info.get("industry", "Unknown industry")

    @property
    def sector(self) -> str:
        return self.info.get("sector", "Unknown sector")
