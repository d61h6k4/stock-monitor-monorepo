from stock_monitor_data.models import Stock


def crypto(period, interval) -> list[Stock]:
    return [
        Stock(
            ticker_name="HUT",
            period=period,
            interval=interval,
            description="""Crypto miner.""",
        ),
        Stock(
            ticker_name="COIN",
            period=period,
            interval=interval,
            description="""Coinbase.""",
        ),
        Stock(
            ticker_name="GBTC",
            period=period,
            interval=interval,
            description="""Tip of the hat to the acid man Hugh Hendry for this idea, but the Grayscale Bitcoin Trust
                             (GBTC) is trading at a 31% discount to NAV. And with Blackrock`s recent approval for a
                             BTC ETF and GBTC`s lawsuit against the SEC for the seemingly arbitrary blocking of its
                             ETF. It`s becoming increasingly probable they get greenlighted and this gap to NAV gets
                             closed..""",
        ),
    ]
