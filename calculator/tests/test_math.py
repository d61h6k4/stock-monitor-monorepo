from typing import NamedTuple

import pandas as pd
import pytest
from bytewax.dataflow import Dataflow
from bytewax.testing import TestingInput, TestingOutput, run_main
from yfinance import Ticker

from calculator.math import AverageTrueRange, AverageDirectionalIndex, MACD, RSI


@pytest.fixture
def msft(shared_datadir):
    if not (shared_datadir / "msft.pkl").exists():
        df = Ticker("MSFT").history(period="1y", interval="1d")
        df.to_pickle(shared_datadir / "msft.pkl")

    return pd.read_pickle(shared_datadir / "msft.pkl")


class TickerPrice(NamedTuple):
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    dividends: float
    kind: str = "TICKER_PRICE"


@pytest.fixture
def msft_flow(msft):
    flow = Dataflow()
    flow.input(
        "msft",
        TestingInput(
            map(
                lambda date_values: (
                    "MSFT",
                    TickerPrice(
                        symbol="MSFT",
                        date=date_values[0].to_pydatetime().isoformat(),
                        open=date_values[1]["Open"],
                        high=date_values[1]["High"],
                        low=date_values[1]["Low"],
                        close=date_values[1]["Close"],
                        volume=date_values[1]["Volume"],
                        dividends=date_values[1]["Dividends"],
                    )._asdict(),
                ),
                msft.iterrows(),
            )
        ),
    )
    return flow


def test_atr_smoke(msft_flow):
    AverageTrueRange(14)(msft_flow)

    results = []
    msft_flow.output("out", TestingOutput(results))

    run_main(msft_flow)

    trs = []
    atrs = []
    for _, x in results:
        trs.append(x["tr"])
        atrs.append(x["atr"])
    assert all((tr >= 0 for tr in trs))
    assert abs(sum(trs[-15:]) / 14.0 - atrs[-1]) < 0.1


def test_adx_smoke(msft_flow):
    AverageTrueRange(14)(msft_flow)
    AverageDirectionalIndex(14)(msft_flow)

    results = []
    msft_flow.output("out", TestingOutput(results))

    run_main(msft_flow)

    pdis = []
    ndis = []
    adxs = []
    for _, x in results:
        pdis.append(x["pdi"])
        ndis.append(x["ndi"])
        adxs.append(x["adx"])

    assert all((x >= 0 for x in pdis))
    assert all((x >= 0 for x in ndis))
    assert all((x >= 0 for x in adxs))


def test_macd_smoke(msft_flow):
    MACD()(msft_flow)

    results = []
    msft_flow.output("out", TestingOutput(results))

    run_main(msft_flow)
    assert results


def test_rsi_smoke(msft_flow):
    RSI()(msft_flow)

    results = []
    msft_flow.output("out", TestingOutput(results))

    run_main(msft_flow)
    assert results
