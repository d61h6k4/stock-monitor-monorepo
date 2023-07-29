from stock_monitor_data.models import Stock


def oil_and_gas_stocks(period, interval) -> list[Stock]:
    return [
        Stock(
            ticker_name="E",
            period=period,
            interval=interval,
            description="""Market Cap: 44.38B. P/E: 245x. Dividend: 8.24%. Insider Ownership: 32%. P/B: 0.69x""",
        ),
        Stock(
            ticker_name="EC",
            period=period,
            interval=interval,
            description=r"""- Market Cap: 37B. Forward P/E: 8.89x. Dividend: 5.85%. P/B: 2x""",
        ),
        Stock(
            ticker_name="EQNR",
            period=period,
            interval=interval,
            description="""Market Cap: 52.4B. Forward P/E: 8.54x. P/B: 1.20x. Dividend: 7.04%. Insider Ownership: 67%""",
        ),
        Stock(
            ticker_name="PCCYF",
            period=period,
            interval=interval,
            description="""Market Cap: 131B. Forward P/E: 10.58x. P/B: 0.39x. Dividend: 6.24%. Insider Ownership: 86%""",
        ),
        Stock(
            ticker_name="SSL",
            period=period,
            interval=interval,
            description="Market Cap: 7B. Forward P/E: 4.06x. P/B: 0.37x. Dividend: 9.96%",
        ),
        Stock(
            ticker_name="YPF",
            period=period,
            interval=interval,
            description="""Market Cap: 4B. Forward P/E: 19.52x. P/B: 0.34x. Dividend: 1.92%""",
        ),
        Stock(
            ticker_name="XES",
            period=period,
            interval=interval,
            description="""S&P Oil & Gas Equipment & Services Select Industry Index""",
        ),
        Stock(
            ticker_name="CNQ",
            period=period,
            interval=interval,
            description="""Canadian Natural Resources Limited""",
        ),
        Stock(
            ticker_name="PSK.TO",
            period=period,
            interval=interval,
            description="""[Source](https://specialsituationinvesting.substack.com/p/prairiesky-royalty-prekf)""",
        ),
        Stock(
            ticker_name="KIST.L",
            period=period,
            interval=interval,
            description="""[Source](https://hiddenvaluegems.com/on-markets-investing/tpost/hv3b9p62m1-hidden-sea-treasure-founder-led-european)""",
        ),
        Stock(
            ticker_name="JOY.TO",
            period=period,
            interval=interval,
            description=r"""[Initial idea](https://bisoninterests.substack.com/p/alex-verge-is-bringing-his-winning)
                              [Update](https://bisoninterests.substack.com/p/100-million-alberta-power-generation)
             """,
        ),
        Stock(
            ticker_name="OXY",
            period=period,
            interval=interval,
            description=r"""Buffet's choice.
                              [Source](https://eaglepointcapital.substack.com/p/occidental-what-does-buffett-see)""",
        ),
        Stock(
            ticker_name="NRP",
            period=period,
            interval=interval,
            description=r"""Coal is not going anywhere.
                              [Source](https://specialsituationinvesting.substack.com/p/coals-resilient-future-nrp)""",
        ),
        Stock(
            ticker_name="CQP",
            period=period,
            interval=interval,
            description=r"""LNG.
                              [Source](https://specialsituationinvesting.substack.com/p/cheniere-energy-partners-cqp)
                            """,
        ),
    ]
