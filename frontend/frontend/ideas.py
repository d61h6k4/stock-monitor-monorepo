import os
from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from typing import Any, NamedTuple, Sequence

import altair as alt
import streamlit as st
from numerize.numerize import numerize

from psycopg2.errors import UndefinedTable

from frontend.utils import escape_markdown


def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "--postgres_host",
        help="Specify host of the postgres server.",
        default=os.getenv("POSTGRES_HOST"),
    )
    parser.add_argument(
        "--postgres_user",
        help="Specify user name of the posgres server.",
        default=os.getenv("POSTGRES_USER"),
    )
    parser.add_argument(
        "--postgres_db",
        help="Specify DB name to connect.",
        default=os.getenv("POSTGRES_DB"),
    )
    parser.add_argument(
        "--postgres_password",
        help="Specify user password of the postgres server.",
        default=os.getenv("POSTGRES_PASSWORD"),
    )

    return parser.parse_args()


class Ticker(NamedTuple):
    symbol: str
    forecast_price: float
    forecast_date: datetime
    market_cap: float
    business_summary: str
    description: str
    industry: str
    sector: str
    in_portfolio: bool
    adx: float = 0.0
    pdi: float = 0.0
    ndi: float = 0.0
    rsi: float = 0.0
    macd: float = 0.0
    macd_signal: float = 0.0
    current_price: float = 0.0
    dividends: float = 0.0
    score: float = 0.0
    moving_average_50: float = 0.0
    moving_average_200: float = 0.0
    money_flow_index: float = 0.0
    coppock_curve: float = 0.0


class RetrieveServicer:
    def __init__(self, conn: st.connections.SQLConnection) -> None:
        self.conn = conn

    def retrieve(self) -> Sequence[Ticker]:
        tickers = []
        try:
            for _, row in self.conn.query(
                "SELECT * FROM tickers", ttl=timedelta(minutes=1)
            ).iterrows():
                tickers.append(
                    Ticker(
                        symbol=row["symbol"],
                        forecast_price=row["forecast_price"],
                        forecast_date=row["forecast_date"],
                        market_cap=row["market_cap"],
                        business_summary=row["business_summary"],
                        description=row["description"],
                        industry=row["industry"],
                        sector=row["sector"],
                        in_portfolio=row["in_portfolio"],
                    )
                )

        except UndefinedTable as e:
            st.error(repr(e))
        return tickers


class FilterServicer:
    def __init__(
        self, ticker_name: str, only_in_portfolio: bool, industry: str, sector: str
    ) -> None:
        self.ticker_name = ticker_name.upper()
        self.only_in_portfolio = only_in_portfolio
        self.industry = set(industry)
        self.sector = set(sector)

    def filter(self, candidates: Sequence[Ticker]) -> Sequence[Ticker]:
        if self.ticker_name:
            return [x for x in candidates if x.symbol.upper() == self.ticker_name]
        if self.only_in_portfolio:
            return [x for x in candidates if x.in_portfolio]
        if self.industry:
            candidates = [x for x in candidates if x.industry in self.industry]
        if self.sector:
            candidates = [x for x in candidates if x.sector in self.sector]

        return candidates


class ScoreServicer:
    def __init__(self, connection: st.connections.SQLConnection) -> None:
        self.conn = connection

    def score(self, candidates: Sequence[Ticker]) -> Sequence[Ticker]:
        return sorted(
            self._score(self._enrich(candidates)), key=lambda c: c.score, reverse=True
        )

    def _score(self, candidates: Sequence[Ticker]) -> Sequence[Ticker]:
        def predict(candidate: Ticker) -> float:
            score = 0.0

            score += 2.0 * (1.0 if candidate.pdi > candidate.ndi else -1.0)
            score += 1.0 * (1.0 if candidate.macd > candidate.macd_signal else -1.0)
            score += 0.5 * (1.0 if candidate.rsi < 75 else -1.0)
            score += 0.5 * (1.0 if candidate.money_flow_index < 80 else -1.0)
            score += 2.0 * (
                1.0
                if candidate.moving_average_50 > candidate.moving_average_200
                else -1.0
            )
            score += 1.0 * (1.0 if candidate.coppock_curve > 0.0 else -1.0)

            return score

        return [
            candidate._replace(score=predict(candidate)) for candidate in candidates
        ]

    def _enrich(self, candidates: Sequence[Ticker]) -> Sequence[Ticker]:
        symbols = {candidate.symbol: candidate for candidate in candidates}
        if not symbols:
            return candidates

        df = self.conn.query(
            """SELECT 
                DISTINCT ON (symbol) symbol, 
                date, 
                close, 
                macd, 
                rsi, 
                adx, 
                pdi, 
                ndi, 
                macd_signal, 
                dividends,
                moving_average_50,
                moving_average_200,
                money_flow_index,
                coppock_curve
               FROM history 
               WHERE symbol IN :symbols 
               ORDER BY symbol, date DESC
            """,
            params={"symbols": tuple(symbols.keys())},
            ttl=timedelta(minutes=1),
        )

        enriched = []
        for _, row in df.iterrows():
            candidate = symbols[row["symbol"]]
            enriched.append(
                candidate._replace(
                    current_price=row["close"],
                    adx=row["adx"],
                    macd=row["macd"],
                    rsi=row["rsi"],
                    pdi=row["pdi"],
                    ndi=row["ndi"],
                    macd_signal=row["macd_signal"],
                    dividends=row["dividends"],
                    moving_average_50=row["moving_average_50"],
                    moving_average_200=row["moving_average_200"],
                    money_flow_index=row["money_flow_index"],
                    coppock_curve=row["coppock_curve"],
                )
            )

        return enriched


def show_ticker(container: Any, ticker: Ticker):
    with container:
        st.title(f"[{ticker.symbol}](/?symbol={ticker.symbol})")
        st.caption(ticker.business_summary)
        st.markdown(escape_markdown(ticker.description))

        (
            col_forecast,
            col_adx,
            col_macd,
            col_rsi,
            col_market_cap,
        ) = st.columns(5)

        with col_forecast:
            st.metric(
                "Forecast",
                f"${ticker.forecast_price:,.2f}",
                delta=ticker.forecast_price - ticker.current_price,
            )
        with col_adx:
            st.metric(
                "ADX",
                ticker.adx,
                delta=ticker.pdi - ticker.ndi,
            )
        with col_macd:
            st.metric(
                "MACD",
                ticker.macd,
                delta=ticker.macd - ticker.macd_signal,
            )

        with col_rsi:
            rsi_color = "off"
            if ticker.rsi > 75:
                rsi_color = "inverse"
            elif ticker.rsi < 25:
                rsi_color = "normal"
            st.metric("RSI", ticker.rsi, delta=ticker.rsi, delta_color=rsi_color)

        with col_market_cap:
            st.metric("Market capitalization", f"${numerize(ticker.market_cap)}")


def show_history(connection: st.connections.SQLConnection, symbol: str):
    with st.sidebar:
        period = st.date_input(
            "Period", value=datetime.now(tz=timezone.utc) - timedelta(weeks=52)
        )
        interval = st.selectbox("Interval", options=["day", "week", "month"])

    columns = [
        "pdi",
        "ndi",
        "adx",
        "macd",
        "macd_signal",
        "rsi",
        "dividends",
        "moving_average_50",
        "moving_average_200",
        "money_flow_index",
        "swing_low",
        "coppock_curve",
    ]
    avg_columns = ",".join([f"AVG({x}) AS {x}" for x in columns])
    df = connection.query(
        f"""
        SELECT
            symbol,
            interval as date,
            MAX(interval_open) AS open,
            MAX(high) AS high,
            MIN(low) AS low,
            MAX(interval_close) AS close,
            SUM(volume) AS volume,
            {avg_columns}
        FROM (
            SELECT
              FIRST_VALUE(open) OVER(PARTITION BY interval ORDER BY interval) AS interval_open,
              LAST_VALUE(close) OVER(PARTITION BY interval ORDER BY interval) AS interval_close,
              *
            FROM (
                SELECT 
                    date_trunc(:interval, date) as interval,
                    *
                FROM history 
                WHERE symbol = :symbol AND date > :date
            )
        )
        GROUP BY symbol, interval
        ORDER BY interval
        ;
        """,
        params={
            "interval": interval,
            "symbol": symbol,
            "date": period,
        },
    )

    def base_chart():
        open_close_color = alt.condition(
            "datum.open <= datum.close", alt.value("#06982d"), alt.value("#ae1325")
        )

        base = alt.Chart(df).encode(
            alt.X("date:T", axis=alt.Axis(title=None)), color=open_close_color
        )

        rule = base.mark_rule().encode(
            alt.Y("low:Q", title=f"{symbol}", scale=alt.Scale(zero=False)),
            alt.Y2("high:Q"),
        )

        bar = base.mark_bar().encode(alt.Y("open:Q"), alt.Y2("close:Q"))

        ma50 = base.mark_line(stroke="#61BFAD", strokeDash=[1, 5]).encode(
            alt.Y("moving_average_50:Q"),
            tooltip=[alt.Tooltip("moving_average_50", title="MA(50)")],
        )
        ma200 = base.mark_line(stroke="#167C80", strokeDash=[1, 5]).encode(
            alt.Y("moving_average_200:Q"),
            tooltip=[alt.Tooltip("moving_average_200", title="MA(200)")],
        )

        swing_low_line = base.mark_line(stroke="#ae1325", strokeDash=[1, 2]).encode(
            y=alt.datum(df.tail(1)["swing_low"].values[0])
        )

        chart = rule + bar + ma50 + ma200 + swing_low_line
        volume_chart = base.mark_bar().encode(alt.Y("volume:Q"))

        return (chart, volume_chart)

    def macd_chart():
        open_close_color = alt.condition(
            "datum.macd_signal <= datum.macd",
            alt.value("#06982d"),
            alt.value("#ae1325"),
        )

        base = alt.Chart(df).encode(
            alt.X("date:T", axis=alt.Axis(title=None)), color=open_close_color
        )
        bar = (
            base.mark_bar()
            .encode(alt.Y("macd_rule:Q", axis=alt.Axis(title="MACD")))
            .transform_calculate(macd_rule="datum.macd - datum.macd_signal")
        )

        return bar

    def adx_chart():
        base = alt.Chart(df).encode(alt.X("date:T", axis=alt.Axis(title=None)))

        adx_line = base.mark_line(stroke="#008FD3").encode(
            alt.Y("adx:Q", axis=alt.Axis(title="ADX")),
            tooltip=[alt.Tooltip("adx", title="ADX")],
        )
        pdi_line = base.mark_line(stroke="#06982d").encode(
            alt.Y("pdi:Q"),
            tooltip=[alt.Tooltip("pdi", title="+DI")],
        )
        ndi_line = base.mark_line(stroke="#ae1325").encode(
            alt.Y("ndi:Q"),
            tooltip=[alt.Tooltip("ndi", title="-DI")],
        )

        return adx_line + pdi_line + ndi_line

    def rsi_chart():
        base = alt.Chart(df).encode(alt.X("date:T", axis=alt.Axis(title=None)))

        rsi_line = base.mark_line(stroke="#008FD3").encode(
            alt.Y("rsi:Q", axis=alt.Axis(title="RSI")),
            tooltip=[alt.Tooltip("rsi", title="RSI")],
        )
        buy_line = base.mark_line(stroke="#ae1325", strokeDash=[1, 2]).encode(
            y=alt.datum(75.0)
        )
        sell_line = base.mark_line(stroke="#06982d", strokeDash=[1, 2]).encode(
            y=alt.datum(25.0)
        )

        return rsi_line + buy_line + sell_line

    def mfi_chart():
        base = alt.Chart(df).encode(alt.X("date:T", axis=alt.Axis(title=None)))

        mfi_line = base.mark_line(stroke="#008FD3").encode(
            alt.Y("money_flow_index:Q", axis=alt.Axis(title="MFI")),
            tooltip=[alt.Tooltip("money_flow_index", title="MFI")],
        )
        buy_line = base.mark_line(stroke="#ae1325", strokeDash=[1, 2]).encode(
            y=alt.datum(80.0)
        )
        sell_line = base.mark_line(stroke="#06982d", strokeDash=[1, 2]).encode(
            y=alt.datum(20.0)
        )

        return mfi_line + buy_line + sell_line

    def coppock_curve_chart():
        open_close_color = alt.condition(
            alt.datum.coppock_curve > 0,
            alt.value("#06982d"),
            alt.value("#ae1325"),
        )

        base = alt.Chart(df).encode(
            alt.X("date:T", axis=alt.Axis(title=None)), color=open_close_color
        )
        bar = base.mark_bar().encode(
            alt.Y("coppock_curve:Q", axis=alt.Axis(title="Coppock Curve"))
        )

        return bar

    chart, volume_chart = base_chart()

    with st.container():
        st.title(symbol)
        st.altair_chart(
            alt.vconcat(
                chart.properties(width=1420),
                volume_chart.properties(height=100, width=1420),
                macd_chart().properties(height=100, width=1420),
                adx_chart().properties(height=100, width=1420),
                rsi_chart().properties(height=100, width=1420),
                mfi_chart().properties(height=100, width=1420),
                coppock_curve_chart().properties(height=100, width=1420),
            ),
            theme="streamlit",
            use_container_width=True,
        )


def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    args = parse_args()
    conn_info = f"postgresql://{args.postgres_user}:{args.postgres_password}@{args.postgres_host}:5432/{args.postgres_db}"
    conn = st.experimental_connection("sql", type="sql", url=conn_info)

    query_params = st.experimental_get_query_params()
    if "symbol" in query_params:
        assert len(query_params["symbol"]) == 1, query_params
        show_history(conn, query_params["symbol"][0])
    else:
        with st.sidebar:
            ticker_name = st.text_input("Ticker", value="", max_chars=12)
            only_in_portfolio = st.toggle("Only portfolio stocks.")
            industry = st.multiselect(
                "Select industry",
                options=conn.query(
                    "SELECT DISTINCT industry FROM tickers"
                ).industry.values,
            )
            sector = st.multiselect(
                "Select sector",
                options=conn.query("SELECT DISTINCT sector FROM tickers").sector.values,
            )

        with st.spinner("Generating candidates..."):
            candidates = ScoreServicer(connection=conn).score(
                FilterServicer(
                    ticker_name=ticker_name,
                    only_in_portfolio=only_in_portfolio,
                    sector=sector,
                    industry=industry,
                ).filter(RetrieveServicer(conn).retrieve())
            )

        pagination = st.container()

        bottom_menu = st.columns((4, 1, 1))
        with bottom_menu[2]:
            batch_size = st.selectbox("Page Size", options=[3, 5, 10])
        with bottom_menu[1]:
            total_pages = (
                int(len(candidates) / batch_size)
                if int(len(candidates) / batch_size) > 0
                else 1
            )
            current_page = st.number_input(
                "Page", min_value=1, max_value=total_pages, step=1
            )
        with bottom_menu[0]:
            st.markdown(f"Page **{current_page}** of **{total_pages}** ")

        if total_pages > 0:
            start_index = (current_page - 1) * batch_size
            for candidate in candidates[start_index : start_index + batch_size]:
                show_ticker(pagination, candidate)
        else:
            with pagination:
                st.info("There is no ticker.")


main()
