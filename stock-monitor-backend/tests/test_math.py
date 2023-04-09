import numpy as np
import pytest
from pandas import DataFrame, read_pickle

from stock_monitor_backend.math import (
    average_true_range,
    best_price_in_period,
    cot_index,
    cot_move_index,
    last_atr,
    moving_average,
    moving_average_distance,
)


@pytest.fixture()
def goog_history(shared_datadir) -> DataFrame:
    return read_pickle(shared_datadir / "goog.history.pkl")


@pytest.fixture()
def cot_palladium_history(shared_datadir) -> DataFrame:
    return read_pickle(shared_datadir / "cot.palladium.pkl")


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


def test_cot_index(cot_palladium_history: DataFrame):
    assert np.allclose(cot_index(cot_palladium_history, 42).last(offset="21d").values, [96.85621, 86.63838, 55.13733])


def test_cot_move_index(cot_palladium_history: DataFrame):
    assert np.allclose(cot_move_index(cot_palladium_history, 42).last(offset="21d").values,
                       [12.39564, -10.21783, -31.5010])
