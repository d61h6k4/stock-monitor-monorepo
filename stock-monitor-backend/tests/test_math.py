import pytest
import numpy as np

from stock_monitor_backend.math import average_true_range, last_atr, best_price_in_period
from pandas import read_pickle, DataFrame


@pytest.fixture
def goog_history(shared_datadir) -> DataFrame:
    yield read_pickle(shared_datadir / "goog.history.pkl")


def test_average_true_range(goog_history: DataFrame):
    assert (np.allclose(average_true_range(goog_history).last(offset="3d").values, [3.29299774, 3.79999847, 3.8719986]))


def test_best_price_in_period(goog_history: DataFrame):
    assert np.isclose(best_price_in_period(goog_history), 102.45999)


def test_last_atr(goog_history: DataFrame):
    assert np.isclose(last_atr(goog_history), 3.87199)