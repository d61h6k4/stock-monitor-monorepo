import numpy as np
import pytest
from pandas import DataFrame, read_pickle

from stock_monitor_backend.math import (
    adx,
    average_true_range,
    best_price_in_period,
    cot_index,
    cot_move_index,
    cot_net_position,
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


@pytest.fixture()
def cot_gold_history(shared_datadir) -> DataFrame:
    return read_pickle(shared_datadir / "gold.cot.pkl")


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


def test_cot_net_position(cot_gold_history: DataFrame):
    assert np.allclose(cot_net_position(cot_gold_history)["net"].values[-1], 26359)


def test_cot_index(cot_gold_history: DataFrame):
    assert np.allclose(cot_index(cot_gold_history, 42).values[-3:], [44.13956024, 38.58880005, 48.99448786])


def test_cot_move_index(cot_gold_history: DataFrame):
    assert np.allclose(cot_move_index(cot_gold_history, 42).values[-3:],
                       [11.77236659, -5.55076019, 10.40568781])


def test_adx(goog_history: DataFrame):
    assert adx(goog_history).shape[0] == goog_history.shape[0]
