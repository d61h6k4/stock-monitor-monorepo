"""Collection of the data models."""
import shutil
import tempfile
import zipfile
from typing import Mapping, Sequence
from datetime import datetime
from pathlib import Path

import pandas as pd
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

cot_session = CachedLimiterSession(
    expire_after=7 * 24 * 3600,
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache(str(Path(__file__).parent.parent.resolve() / "cot.cache")),
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
    history: DataFrame = DataFrame()
    business_summary: str = "NO DATA"
    market_cap: float = 0.0
    expectation: Expectation | None = None
    description: str = ""

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

    @validator("business_summary", always=True)
    def set_business_summary(cls: "Stock", business_summary: str, values: Mapping[str, str]) -> str:
        """Extract business summary."""
        ticker = Ticker(values["ticker_name"], session=session)
        return ticker.get_info().get("longBusinessSummary", business_summary)

    @validator("market_cap", always=True)
    def set_market_cap(cls: "Stock", market_cap: float, values: Mapping[str, str]) -> float:
        """Extract market cap."""
        ticker = Ticker(values["ticker_name"], session=session)
        return ticker.get_info().get("marketCap", market_cap)


class COT(BaseModel):
    """Representation of the Commitment of traders data."""
    since: int
    history: DataFrame = DataFrame()

    class Config:
        """Allow DataFrame."""
        arbitrary_types_allowed = True

    @validator("since")
    def is_valid_since_value(cls: "COT", since: int) -> int:
        """Checks since is year >= 2010."""
        if since < 2010:
            msg = "COT data available only since 2010."
            raise ValueError(msg)
        if since > datetime.today().year:
            msg = "No way to load data from the future"
            raise ValueError(msg)

        return since

    @validator("history", always=True)
    def download_history(cls: "COT",
                         history: DataFrame,
                         values: Mapping[str, int]) -> DataFrame:
        """Downloads the data."""

        def download_file(url, destination_dir):
            local_filename = destination_dir / url.split('/')[-1]
            with cot_session.get(url, stream=False) as r, open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            return local_filename

        def load_combine_reports_per_year(year: int) -> DataFrame:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = Path(temp_dir)
                path_to_zip_file = download_file(f"https://www.cftc.gov/files/dea/history/dea_com_xls_{year}.zip",
                                                 temp_dir)

                with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir / "data")

                return pd.read_excel(temp_dir / "data/annualof.xls")

        def load_combine_reports_since_year(year: int) -> DataFrame:
            dfs = []

            for dt in range(year, datetime.today().year + 1):
                dfs.append(load_combine_reports_per_year(dt))

            return pd.concat(dfs)

        assert history.empty

        return load_combine_reports_since_year(values["since"])

    @staticmethod
    def commercials_by_names_or_codes(df: DataFrame, names: Sequence[str] | None = None,
                                      codes: Sequence[int] | None = None) -> DataFrame:
        """Returns commercials data from `df`."""
        assert names or codes, "Function requires to be provided or names or codes."
        assert "Comm_Positions_Long_All" in df.columns
        assert "Comm_Positions_Short_All" in df.columns

        if not names:
            names = []
        if not codes:
            codes = []

        return_columns = ["Market_and_Exchange_Names", "CFTC_Commodity_Code", "Report_Date_as_MM_DD_YYYY",
                          "Comm_Positions_Long_All", "Comm_Positions_Short_All", "Open_Interest_All",
                          "NonComm_Positions_Long_All", "NonComm_Positions_Short_All", "NonRept_Positions_Long_All",
                          "NonRept_Positions_Short_All"]
        return df[return_columns].query("Market_and_Exchange_Names == @names or CFTC_Commodity_Code == @codes")


class Arbitrage(BaseModel):
    class Config:
        """Allow DataFrame."""
        arbitrary_types_allowed = True

    target: Stock
    buyer: Stock | str
    offer_price: float
    additional_buyer_ratio: float
    expecting_closing: datetime
    commentary: str
