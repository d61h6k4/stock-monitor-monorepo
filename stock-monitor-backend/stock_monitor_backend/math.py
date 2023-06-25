"""Collection of math funtions."""
import pandas as pd
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


def cot_net_position(df: DataFrame) -> DataFrame:
    """Returns Net position of commercials."""
    cdf = df[["Report_Date_as_MM_DD_YYYY", "Comm_Positions_Long_All", "Comm_Positions_Short_All",
              "NonComm_Positions_Long_All", "NonComm_Positions_Short_All", "NonRept_Positions_Long_All",
              "NonRept_Positions_Short_All"]] \
        .set_index(DatetimeIndex(df["Report_Date_as_MM_DD_YYYY"]).to_period("w")) \
        .groupby(level=0).sum(numeric_only=True)

    cdf["commercials"] = cdf["Comm_Positions_Long_All"] - cdf["Comm_Positions_Short_All"]
    cdf["funds"] = cdf["NonComm_Positions_Long_All"] - cdf["NonComm_Positions_Short_All"]
    cdf["small traders"] = cdf["NonRept_Positions_Long_All"] - cdf["NonRept_Positions_Short_All"]

    cdf.drop(columns=["Comm_Positions_Long_All", "Comm_Positions_Short_All",
                      "NonComm_Positions_Long_All", "NonComm_Positions_Short_All",
                      "NonRept_Positions_Long_All",
                      "NonRept_Positions_Short_All"], inplace=True)
    return cdf.stack() \
        .reset_index() \
        .rename(columns={"level_1": "cot_type", 0: "net"}) \
        .set_index("Report_Date_as_MM_DD_YYYY")


def cot_index(df: DataFrame, p: int, traders: str = "commercials") -> Series:
    """Returns COT index.

    100 * (net - min_net) / (max_net - min_net), max and min within period.
    """
    assert traders in ["commercials", "funds", "small traders"]

    net = cot_net_position(df).query("cot_type == @traders")["net"]
    windo_df = net.rolling(p, 1)
    return 100.0 * ((net - windo_df.min()) / (windo_df.max() - windo_df.min()))


def cot_move_index(df: DataFrame, p: int) -> Series:
    """Returns COT move index.

    COT index change week to week.
    """
    return cot_index(df, p).diff()


def macd(df: DataFrame) -> Series:
    """Returns MACD values.

    https://www.investopedia.com/terms/m/macd.asp
    """
    assert "Close" in df.columns
    return df["Close"].ewm(alpha=1. / 12.).mean() - df["Close"].ewm(alpha=1. / 26.).mean()


def rsi(df: DataFrame) -> Series:
    """Returns RSI values.

    https://www.investopedia.com/terms/r/rsi.asp
    """
    assert "Close" in df.columns
    gain = df["Close"].pct_change().clip(lower=0.0)
    average_gain = (gain.ewm(alpha=1. / 14.).mean())
    loss = df["Close"].pct_change().clip(upper=0.0) * -1.0
    average_loss = loss.ewm(alpha=1. / 14.).mean()
    return 100 - (100 / (1.0 + average_gain / average_loss)).fillna(0.0)


def adx(df: DataFrame) -> DataFrame:
    """Returns ADX, +DI and -DI.

    https://www.investopedia.com/terms/a/adx.asp
    """
    assert isinstance(df.index, DatetimeIndex)
    assert "High" in df.columns
    assert "Low" in df.columns
    assert "Close" in df.columns

    pdm = df["High"].diff().clip(lower=0.0)
    ndm = df["Low"].diff().clip(upper=0.0)
    atr = average_true_range(df, p=14)

    pdi = 100 * (pdm.ewm(alpha=1 / 14.).mean() / atr)
    ndi = abs(100 * (ndm.ewm(alpha=1 / 14.).mean() / atr))
    dx = (abs(pdi - ndi) / abs(pdi + ndi)) * 100
    adx_smooth = (((dx.shift(1) * (14. - 1)) + dx) / 14.).ewm(alpha=1 / 14.).mean()

    return pd.concat([pdi, ndi, adx_smooth], axis=1) \
        .rename(columns={0: "+di", 1: "-di", 2: "adx"}) \
        .fillna(0.0)
