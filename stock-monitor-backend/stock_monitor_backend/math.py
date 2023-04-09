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


def moving_average(df: DataFrame, p: int) -> Series:
    """Moving average in p days."""
    assert "Close" in df.columns
    return df["Close"].rolling(p).mean()


def moving_average_distance(df: DataFrame, fast_ma: int, slow_ma: int) -> float:
    """Moving average in p days."""
    assert "Close" in df.columns
    return moving_average(df, fast_ma).last(offset="1D").max() / moving_average(df, slow_ma).last(offset="1D").max()


def cot_index(df: DataFrame, p: int) -> Series:
    """Returns COT index.

    100 * (net - min_net) / (max_net - min_net), max and min within period.
    """
    cdf = df[["Report_Date_as_MM_DD_YYYY", "Comm_Positions_Long_All", "Comm_Positions_Short_All"]] \
        .set_index("Report_Date_as_MM_DD_YYYY").sort_index()
    cdf["net"] = cdf["Comm_Positions_Long_All"] - cdf["Comm_Positions_Short_All"]
    windo_df = cdf["net"].rolling(f"{p}d")

    return (100 * (cdf["net"] - windo_df.min()) / (windo_df.max() - windo_df.min())).rename("cot_index")


def cot_move_index(df: DataFrame, p: int) -> Series:
    """Returns COT move index.

    COT index change week to week.
    """
    return cot_index(df, p).diff().rename("cot_move_index")
