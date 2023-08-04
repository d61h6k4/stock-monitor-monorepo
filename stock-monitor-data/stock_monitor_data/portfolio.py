from itertools import chain
from datetime import datetime, timezone
from stock_monitor_data.models import Stock, Expectation
from stock_monitor_data.ideas import ideas
from stock_monitor_data.oil_and_gas import oil_and_gas_stocks


def portfolio(period: str, interval: str):
    tickers = {
        "TGNA": {
            "buy_date": datetime(2022, 12, 1, tzinfo=timezone.utc),
            "confidence": 0.75,
        },
        "SOMA.V": {
            "buy_date": datetime(2023, 4, 17, tzinfo=timezone.utc),
            "confidence": 0.1,
        },
        "TM.V": {
            "buy_date": datetime(2023, 4, 17, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "APR.WA": {
            "buy_date": datetime(2023, 6, 27, tzinfo=timezone.utc),
            "confidence": 0.3,
        },
        "PSK.TO": {
            "buy_date": datetime(2023, 7, 10, tzinfo=timezone.utc),
            "confidence": 0.3,
        },
        "APT": {
            "buy_date": datetime(2023, 8, 2, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "ANTM.JK": {
            "buy_date": datetime(2023, 8, 3, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
    }

    res = []
    for ticker in chain.from_iterable(
        [ideas(period, interval), oil_and_gas_stocks(period, interval)]
    ):
        if ticker.ticker_name in tickers:
            assert ticker.expectation, ticker
            new_expectation = ticker.expectation.model_copy(
                update={"confidence": tickers[ticker.ticker_name]["confidence"]}
            )
            res.append(
                ticker.model_copy(
                    update={
                        "expectation": new_expectation,
                        "buy_date": tickers[ticker.ticker_name]["buy_date"],
                    }
                )
            )
    return res
