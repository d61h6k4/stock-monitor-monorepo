"""Collection of math funtions."""

from pandas import DataFrame, DatetimeIndex, Series


def average_true_range(df: DataFrame, p: int = 5) -> Series:
    """Average true range (ATR).

    First, we calculate the true range, then we take the moving average of our true
    range value for the average true range.
    """
    assert isinstance(df.index, DatetimeIndex)
    assert "High" in df.columns
    assert "Low" in df.columns
    assert "Close" in df.columns

    return (DataFrame([df["High"] - df["Low"],
                       (df["High"] - df["Close"].shift(1)).fillna(0.0),
                       (df["Close"].shift(1) - df["Low"]).fillna(0.0)])
            .T.max(axis=1).rolling(p).mean().rename_axis("atr"))


def last_atr(df: DataFrame, p: int = 5) -> float:
    """Returns last average true range value."""
    return average_true_range(df, p).last(offset="1D").max()


def best_price_in_period(df: DataFrame, p: int = 14) -> float:
    """Best price in the given period."""
    assert "Close" in df.columns
    return df["Close"].last(offset=f"{p}D").max()
