import os
import sqlite3

import mplfinance
import pandas as pd
import streamlit as st
from pandas import DataFrame

st.set_page_config(layout="wide")


def query_to_symbol(query: str) -> str:
    return query


@st.cache_resource
def connection():
    db_uri = os.getenv("DB_URI")
    assert db_uri is not None, "Please specify path to the db via DB_URI."
    return sqlite3.connect(db_uri)


@st.cache_data
def get_tickers_history(symbol: str) -> DataFrame:
    con = connection()
    cur = con.cursor()
    columns = [
        "symbol",
        "date",
        "open",
        "high",
        "close",
        "low",
        "pdi",
        "ndi",
        "adx",
        "macd",
        "macd_signal",
        "rsi",
    ]
    cur.execute(f"SELECT {','.join(columns)} FROM history WHERE symbol = ?", (symbol,))
    return (
        DataFrame(cur.fetchall(), columns=columns)
        .assign(date=lambda df: pd.to_datetime(df["date"]))
        .set_index("date")
    )


def plot_price(df: DataFrame):
    GREEN = "#70a800"
    RED = "#ea0070"
    BLUE = "#005397"
    apdict = [
        mplfinance.make_addplot(
            df["adx"], panel=1, label="ADX", color=BLUE, secondary_y=False
        ),
        mplfinance.make_addplot(
            df["pdi"], panel=1, label="+DI", color=GREEN, secondary_y=False
        ),
        mplfinance.make_addplot(
            df["ndi"], panel=1, label="-DI", color=RED, secondary_y=False
        ),
        mplfinance.make_addplot(
            df["macd"], panel=2, label="MACD", color=GREEN, secondary_y=False
        ),
        mplfinance.make_addplot(
            df["macd_signal"], panel=2, label="signal", color=RED, secondary_y=False
        ),
        mplfinance.make_addplot(
            (df["macd"] - df["macd_signal"]).clip(upper=0.0),
            panel=2,
            type="bar",
            color=RED,
            secondary_y=False,
        ),
        mplfinance.make_addplot(
            (df["macd"] - df["macd_signal"]).clip(lower=0.0),
            panel=2,
            type="bar",
            color=GREEN,
            secondary_y=False,
        ),
        mplfinance.make_addplot(df["rsi"], panel=3, color=BLUE, label="RSI"),
    ]

    fig, axs = mplfinance.plot(
        df,
        style="binance",
        type="candle",
        addplot=apdict,
        returnfig=True,
        figscale=1.2,
        figsize=(20, 9),
    )

    axs[6].axhline(y=70, linestyle="-", linewidth=0.8, color="#B7E3E4")
    axs[6].axhline(y=30, linestyle="-", linewidth=0.8, color="#E88565")

    return fig


st.title("Stock-Monitor")

query = st.text_input(":mag_right: Query")

if query:
    symbol = query_to_symbol(query)
    history = get_tickers_history(symbol)
    st.pyplot(plot_price(history))
