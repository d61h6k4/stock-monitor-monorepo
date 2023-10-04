import os
from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from typing import Any, NamedTuple, Sequence

import pandas as pd

import altair as alt
import streamlit as st


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


def show_cot(container: Any, df: pd.DataFrame):
    def base_chart():
        base = alt.Chart(df).encode(alt.X("report_date:T", axis=alt.Axis(title=None)))
        open_interest_line = base.mark_line().encode(
            alt.Y("open_interest_all:Q", axis=alt.Axis(title="CoT"))
        )
        prod_bar = (
            base.mark_bar()
            .transform_calculate(
                producer="datum.prod_merc_positions_long_all - datum.prod_merc_positions_short_all",
                swap="datum.swap_positions_long_all - datum.swap_positions_short_all",
                money_manager="datum.m_money_positions_long_all - datum.m_money_positions_short_all",
                other_rept="datum.other_rept_positions_long_all - datum.other_rept_positions_short_all",
                non_rept="datum.nonrept_positions_long_all - datum.nonrept_positions_short_all",
            )
            .transform_fold(
                fold=["producer", "swap", "money_manager", "other_rept", "non_rept"],
                as_=["variable", "value"],
            )
            .encode(
                alt.Y("sum(value):Q"),
                color=alt.Color("variable:N").scale(
                    domain=[
                        "producer",
                        "swap",
                        "money_manager",
                        "other_rept",
                        "non_rept",
                    ],
                    range=[
                        "#E54B4B",
                        "#9C2525",
                        "#005397",
                        "#0BBCD6",
                        "#F0CF61"
                    ],
                ),
            )
        )
        return open_interest_line + prod_bar

    with container:
        st.altair_chart(
            alt.vconcat(
                base_chart().properties(width=1024),
            ),
            theme="streamlit",
            use_container_width=True,
        )


def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    args = parse_args()
    conn_info = f"postgresql://{args.postgres_user}:{args.postgres_password}@{args.postgres_host}:5432/{args.postgres_db}"
    conn = st.experimental_connection("sql", type="sql", url=conn_info)

    with st.sidebar:
        market_and_exchange_names = conn.query(
            """SELECT 
                DISTINCT ON(market_and_exchange_names) market_and_exchange_names, 
                cftc_commodity_code 
               FROM 
                cot_history
            """,
            ttl=timedelta(hours=1),
        )

        market_and_exchange_names = st.multiselect(
            "Select the market and exchange names",
            options=[
                (n, c)
                for n, c in market_and_exchange_names[
                    ["market_and_exchange_names", "cftc_commodity_code"]
                ].values
            ],
            default=None,
            format_func=lambda nc: f"{nc[0]} (Code {nc[1]})",
        )

        since = st.date_input("Since", value=datetime(2018, 1, 1))

    if market_and_exchange_names:
        df = conn.query(
            """SELECT
                *
               FROM
                 cot_history
               WHERE
                 report_date >= :since AND market_and_exchange_names IN :names
            """,
            params={
                "since": since,
                "names": tuple(n for n, _ in market_and_exchange_names),
            },
            ttl=timedelta(hours=1),
        )

        main = st.container()
        show_cot(main, df)


main()
