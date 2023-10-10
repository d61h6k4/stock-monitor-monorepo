from datetime import datetime, timezone
from itertools import chain

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
        "J4V.F": {
            "buy_date": datetime(2023, 9, 15, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "PKN.WA": {
            "buy_date": datetime(2023, 9, 25, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "APN.WA": {
            "buy_date": datetime(2023, 9, 25, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "GAN": {
            "buy_date": datetime(2023, 9, 28, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "SQM": {
            "buy_date": datetime(2023, 10, 2, tzinfo=timezone.utc),
            "confidence": 0.5,
        },
        "LDO.MI": {
            "buy_date": datetime(2023, 10, 10, tzinfo=timezone.utc),
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

    assert len(res) == len(tickers), set(t.ticker_name for t in res).difference(
        set(tickers.keys())
    )
    return res
