from datetime import datetime, timezone
from stock_monitor_data.models import Stock, Expectation


def portfolio(period: str, interval: str):
    res = []
    for ticker_name in ["TGNA", "SOMA.V", "TM.V", "APR.WA", "PSK.TO", "APT", "ANTM.JK"]:
        buy_date = None
        description = None
        expectation = None
        if ticker_name == "TGNA":
            buy_date = datetime(2022, 12, 1, tzinfo=timezone.utc)
            description = "Arbitrage"
            expectation = Expectation(
                price=24,
                date=datetime(2024, 11, 15, tzinfo=timezone.utc),
                confidence=0.75,
            )
        elif ticker_name == "CEG":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
            description = """Constellation Energy Corporation, formerly Constellation Newholdco, Inc., is a clean
                             energy company. The Company is focused on carbon-free electricity. It is a supplier
                             of clean energy and sustainable solutions to homes, businesses, public sector, community
                             aggregations and a range of wholesale customers, such as municipalities, cooperatives.
                             Utility, energy.
                             See CEG in Ideas.
                          """
            expectation = Expectation(
                price=115,
                date=datetime(2023, 12, 31, tzinfo=timezone.utc),
                confidence=0.5,
            )
        elif ticker_name == "SOMA.V":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Imagine you can invest in gold as a safe haven, but with the characteristics of an exponential tech stock.
                              If Soma Gold proves they have the resources, it could simply expand annual production from 36K to 75K.
                             """
            expectation = Expectation(
                price=6,
                date=datetime(2033, 12, 31, tzinfo=timezone.utc),
                confidence=0.01,
            )
        elif ticker_name == "TM.V":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Trigon Metals Inc. (TM) is a Canadian exploration, development, and mining company focused on copper
                                and silver assets in Africa."""
            expectation = Expectation(
                price=0.6,
                date=datetime(2025, 12, 31, tzinfo=timezone.utc),
                confidence=0.5,
            )
        elif ticker_name == "FTAI":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Aircraft and engine lessor that has gone through a major transformation from a complex “mess” of
                              assets to a pure-play aviation company."""
            expectation = Expectation(
                price=94,
                date=datetime(2027, 12, 31, tzinfo=timezone.utc),
                confidence=0.5,
            )
        elif ticker_name == "CRNT":
            buy_date = datetime(2023, 4, 20, tzinfo=timezone.utc)
            description = r"""Vendor for global wireless network operators specializing in backhaul solutions. Shareholders have
                                recently rejected a hostile takeover by peer \$AVNW at \$3.8/share. Renewed talks between AVNW and CRNT
                                present the potential for near-term upside realization."""
            expectation = Expectation(
                price=3.08,
                date=datetime(2023, 11, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
        elif ticker_name == "ATLX":
            buy_date = datetime(2023, 4, 24, tzinfo=timezone.utc)
            description = r"""Meme stock, lithium :P"""
            expectation = Expectation(
                price=25,
                date=datetime(2023, 9, 15, tzinfo=timezone.utc),
                confidence=0.1,
            )
        elif ticker_name == "FIP":
            buy_date = datetime(2023, 5, 1, tzinfo=timezone.utc)
            expectation = Expectation(
                price=7, date=datetime(2023, 8, 1, tzinfo=timezone.utc), confidence=0.5
            )
            description = r"""Recent spin-off from \$FTAI with 4 infrastructure assets: 3 energy terminals and a railroad business.
                                EBITDA is set to increase from \$140m today to \$250m in the next 12-18 months. FPI`s Jefferson terminal
                                is now on cusp of generating strong earnings. Transtar railroad earnings have been consistently increasing
                                through new business initiatives. Construction of the 485MW power plant at Long Ridge is complete.
                                Downside is well protected at current share price levels."""
        elif ticker_name == "CBD":
            buy_date = datetime(2023, 5, 4, tzinfo=timezone.utc)
            expectation = Expectation(
                price=6,
                date=datetime(2023, 12, 31, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = r"""CBD is a Brazilian holding company that is spinning off its Colombian grocery chain, Grupo Exito,
                              in the second quarter of 2023. """
        elif ticker_name == "SCHW":
            buy_date = datetime(2023, 5, 16, tzinfo=timezone.utc)
            expectation = Expectation(
                price=80,
                date=datetime(2024, 9, 15, tzinfo=timezone.utc),
                confidence=0.3,
            )
            description = r"""SCHW unfairly sold off following the SVB fallout."""
        elif ticker_name == "AMKR":
            buy_date = datetime(2023, 5, 18, tzinfo=timezone.utc)
            expectation = Expectation(
                price=87,
                date=datetime(2023, 12, 31, tzinfo=timezone.utc),
                confidence=0.95,
            )
            description = r"""Semiconductor assembly services provider - the world`s most wonderfully boring businesses to own.
                                At 9x earnings and shifting into higher margin services. For a semi business, it has very low
                                cyclicality and low capex needs, and yet is delivering above-industry revenue growth with 3 year CAGR of 20%."""
        elif ticker_name == "FGH":
            buy_date = datetime(2023, 6, 16, tzinfo=timezone.utc)
            expectation = Expectation(
                price=10,
                date=datetime(2025, 6, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = r"""The current value of the investments, cash, and real estate can be ballparked between ~\$81.7M-\$90.7M,
                          the book value sits at ~\$42.7M and the market cap is \$34M. Sum-of-the-parts story has been the stable
                          thesis for the better part of a year and a half now and hasn`t worked yet. So, the question begs, will it ever?"""
        elif ticker_name == "MMK.VI":
            buy_date = datetime(2023, 6, 16, tzinfo=timezone.utc)
            expectation = Expectation(
                price=193,
                date=datetime(2024, 1, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = r"""Therefore, MMK can be confidently considered between fairly valued to somewhat undervalued
                          (definitely not overvalued in my opinion). Assuming a “normalised” 9x multiple of EBITDA,
                          in a transaction with a strategic buyer MMK could be worth up to \€193 (+41% potential upside)
                          on 2023 consensus numbers."""
        elif ticker_name == "APR.WA":
            buy_date = datetime(2023, 6, 27, tzinfo=timezone.utc)
            expectation = Expectation(
                price=40,
                date=datetime(2025, 1, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = r"""The independent aftermarket (IAM) industry has an anti-cyclical component that generally
                            works well in any economic environment but especially in times of economic downturns.
                            When, due to a crisis, the sale of new vehicles decreases, this causes an increase in
                            the age of the vehicle fleet, resulting in the need for more maintenance."""
        elif ticker_name == "PSK.TO":
            buy_date = datetime(2023, 7, 10, tzinfo=timezone.utc)
            expectation = Expectation(
                price=30,
                date=datetime(2023, 9, 15, tzinfo=timezone.utc),
                confidence=0.1,
            )
            description = r"""Play with Oil."""
        elif ticker_name == "VGIT":
            buy_date = datetime(2023, 7, 21, tzinfo=timezone.utc)
            expectation = Expectation(
                price=65,
                date=datetime(2023, 12, 15, tzinfo=timezone.utc),
                confidence=1.0,
            )
            description = r"""Tresuries."""
        elif ticker_name == "APT":
            buy_date = datetime(2023, 8, 2, tzinfo=timezone.utc)
            expectation = Expectation(
                price=4.5,
                date=datetime(2023, 12, 31, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = "See for more in ideas."
        elif ticker_name == "ANTM.JK":
            buy_date = datetime(2023, 8, 3, tzinfo=timezone.utc)
            expectation = Expectation(
                price=2700,
                date=datetime(2025, 3, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = "Comodity."
        elif ticker_name == "S85.SI":
            buy_date = datetime(2023, 8, 3, tzinfo=timezone.utc)
            expectation = Expectation(
                price=1.029,
                date=datetime(2027, 1, 15, tzinfo=timezone.utc),
                confidence=0.5,
            )
            description = "China reopening."

        assert buy_date is not None, f"No buy_date for {ticker_name}"
        assert description is not None, f"No description for {ticker_name}"
        assert expectation is not None, f"No expectation for {ticker_name}"
        res.append(
            Stock(
                ticker_name=ticker_name,
                period=period,
                interval=interval,
                buy_date=buy_date,
                description=description,
                expectation=expectation,
            )
        )

    return res
