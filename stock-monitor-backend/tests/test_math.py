import pytest
import numpy as np

from stock_monitor_backend.math import average_true_range, last_atr, best_price_in_period, moving_average, \
    moving_average_distance
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


def test_moving_average(goog_history: DataFrame):
    assert np.allclose(moving_average(goog_history, 21).last(offset="3d").values,
                       [93.06952413, 93.36095283, 93.61619096])


def test_moving_average_distance(goog_history: DataFrame):
    assert moving_average_distance(goog_history, 21, 50) < 1.0
