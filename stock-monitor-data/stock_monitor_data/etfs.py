from stock_monitor_data.models import Stock


def etfs(period, interval) -> list[Stock]:
    return [
        Stock(
            ticker_name="JPXN",
            period=period,
            interval=interval,
            description="""Japan.""",
        ),
        Stock(
            ticker_name="DAX",
            period=period,
            interval=interval,
            description="""Germany.""",
        ),
        Stock(
            ticker_name="^SPX", period=period, interval=interval, description="""USA."""
        ),
        Stock(
            ticker_name="^IXIC",
            period=period,
            interval=interval,
            description="""NASDAQ.""",
        ),
        Stock(
            ticker_name="FXI",
            period=period,
            interval=interval,
            description="""China Large Cap.""",
        ),
        Stock(
            ticker_name="ERUS",
            period=period,
            interval=interval,
            description="""Russia.""",
        ),
        Stock(
            ticker_name="XOP",
            period=period,
            interval=interval,
            description="""SPDR S&P Oil & Gas Exploration & Production ETF.""",
        ),
        Stock(
            ticker_name="XLE",
            period=period,
            interval=interval,
            description="""Energy Select Sector SPDR Fund.""",
        ),
        Stock(
            ticker_name="EWZ",
            period=period,
            interval=interval,
            description="""Brazil.""",
        ),
        Stock(
            ticker_name="GXG",
            period=period,
            interval=interval,
            description="""Colombia.""",
        ),
        Stock(
            ticker_name="MSOS",
            period=period,
            interval=interval,
            description="""Canabis.""",
        ),
        Stock(
            ticker_name="VGIT",
            period=period,
            interval=interval,
            description="""Treasuries.""",
        ),
        Stock(
            ticker_name="TUR",
            period=period,
            interval=interval,
            description="""Turkey.""",
        ),
        Stock(
            ticker_name="VNM",
            period=period,
            interval=interval,
            description="""Vietnam.""",
        ),
    ]
