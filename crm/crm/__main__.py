import os
import logging
import psycopg
from argparse import ArgumentParser
from datetime import datetime, timezone


from rich.logging import RichHandler
from rich import progress

from stock_monitor_data.ideas import ideas
from stock_monitor_data.portfolio import portfolio
from stock_monitor_data.models import Stock

LOGGER = logging.getLogger("crm")

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


def create_tables(connection: psycopg.Connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS tickers (
                    symbol VARCHAR(12) NOT NULL PRIMARY KEY,
                    business_summary TEXT,
                    market_cap REAL,
                    forecast_price REAL,
                    forecast_date DATE,
                    description TEXT,
                    in_portfolio BOOL)
                """
        )
        connection.commit()


def insert_if_not_exist(cursor: psycopg.Cursor, stock: Stock):
    try:
        cursor.execute(
        """INSERT INTO tickers (
                symbol,
                business_summary,
                market_cap,
                forecast_price,
                forecast_date,
                description,
                in_portfolio)
            SELECT 
              %s, %s, %s, %s, %s, %s, %s
            WHERE 
              NOT EXISTS (
              SELECT symbol FROM tickers WHERE symbol = %s
             );
        """,
        (
            stock.ticker_name,
            stock.business_summary,
            stock.market_cap,
            stock.expectation.price,
            stock.expectation.date,
            stock.description,
            False,
            stock.ticker_name
        ),
    )
    except Exception as e:
        LOGGER.exception("Failed to insert %s", stock.ticker_name)


def update_in_portfolio(cursor: psycopg.Cursor, stock: Stock):
    cursor.execute(
        """UPDATE tickers 
           SET in_portfolio=%s
           WHERE symbol = %s;
        """,
        (True, stock.ticker_name),
    )


def main():
    
    args = parse_args()

    LOGGER.info("Connecting to %s/%s", args.postgres_host, args.postgres_db)
    conn_info = f"postgresql://{args.postgres_user}:{args.postgres_password}@{args.postgres_host}:5432/{args.postgres_db}"
    with psycopg.connect(conn_info) as conn:
        create_tables(conn)

        with progress.Progress(
            "[progress.description]{task.description}",
            progress.BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            progress.TimeRemainingColumn(),
            progress.TimeElapsedColumn(),
            refresh_per_second=1,  # bit slower updates
        ) as pgs:
            process_stocks_task = pgs.add_task("[green]Processing ideas:", total=None)

            with conn.cursor() as cursor:
                for stock in ideas("1d", "1d"):
                    insert_if_not_exist(cursor, stock)
                    pgs.advance(process_stocks_task)

                    if stock.expectation.date < datetime.now(tz=timezone.utc):
                        LOGGER.critical(
                            "The ticker's forecast date is outdated. %s",
                            stock.ticker_name,
                        )

                conn.commit()

            process_portfolio_task = pgs.add_task(
                "[blue]Processing portfolio:", total=None
            )

            with conn.cursor() as cursor:
                for stock in portfolio("1d", "1d"):
                    update_in_portfolio(cursor, stock)
                    pgs.advance(process_portfolio_task)
                conn.commit()


if __name__ == "__main__":
    logging.basicConfig(handlers=[RichHandler()], level=logging.INFO)
    main()