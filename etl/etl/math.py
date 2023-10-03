import heapq
from typing import Any, Mapping, Tuple

from bytewax.dataflow import Dataflow

KV = Mapping[str, Any]
State = KV


def exponential_moving_average(alpha: float, current: float, ma: float) -> float:
    return alpha * current + (1.0 - alpha) * ma


class AverageTrueRange:
    """Average true range.

    https://www.investopedia.com/terms/a/atr.asp
    """

    def __init__(self, p: float):
        """Constructor.

        Args:
          p - the length of the window.
        """
        self.alpha = 2.0 / (p + 1.0)

    @staticmethod
    def builder() -> State:
        return {"close": None, "atr": None}

    @staticmethod
    def true_range(high: float, low: float, close_prev: float) -> float:
        return max(high - low, abs(high - close_prev), abs(low - close_prev))

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        tr = self.true_range(
            current["high"], current["low"], state["close"] or current["high"]
        )
        atr = exponential_moving_average(self.alpha, tr, state["atr"] or tr)
        current.update({"tr": tr, "atr": atr})
        return current, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Calculate ATR", self.builder, self.mapper)


class AverageDirectionalIndex:
    """Average Directional Index.

    https://www.investopedia.com/terms/a/adx.asp
    """

    def __init__(self, p: float):
        """Constructor.

        Args:
          p - the length of the window."""
        self.alpha = 2.0 / (p + 1.0)
        self.p = p

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[State, KV]:
        up_move = current["high"] - state.get("high", current["high"])
        down_move = state.get("low", current["low"]) - current["low"]
        pdm = up_move if up_move > down_move else 0.0
        ndm = down_move if down_move > up_move else 0.0
        apdm = exponential_moving_average(self.alpha, pdm, state.get("apdm", pdm))
        andm = exponential_moving_average(self.alpha, ndm, state.get("andm", ndm))

        if abs(current["atr"]) < 1e-3:
            pdi = 0.0
            ndi = 0.0
        else:
            pdi = 100.0 * (apdm / current["atr"])
            ndi = 100.0 * (andm / current["atr"])

        if abs(pdi + ndi) < 1e-3:
            dx = 0.0
        else:
            dx = 100.0 * (abs(pdi - ndi) / abs(pdi + ndi))
        adx = exponential_moving_average(self.alpha, dx, state.get("adx", dx))

        current.update({"apdm": apdm, "andm": andm, "pdi": pdi, "ndi": ndi, "adx": adx})
        return current, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Calculate ADX", self.builder, self.mapper)


class MACD:
    """Moving Average Convergence/Divergence.

    https://www.investopedia.com/terms/m/macd.asp
    """

    def __init__(self):
        self.alpha_9 = 2.0 / (9.0 + 1.0)
        self.alpha_12 = 2.0 / (12.0 + 1.0)
        self.alpha_26 = 2.0 / (26.0 + 1.0)

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        c_ma_12 = exponential_moving_average(
            self.alpha_12, current["close"], state.get("close_ma_12", current["close"])
        )
        c_ma_26 = exponential_moving_average(
            self.alpha_26, current["close"], state.get("close_ma_26", current["close"])
        )
        macd = c_ma_12 - c_ma_26

        macd_signal = exponential_moving_average(
            self.alpha_9, macd, state.get("macd_signal", macd)
        )

        current.update(
            {
                "close_ma_12": c_ma_12,
                "close_ma_26": c_ma_26,
                "macd": macd,
                "macd_signal": macd_signal,
            }
        )
        return current, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Calculate MACD", self.builder, self.mapper)


class RSI:
    """Relative Strength Index.

    https://www.investopedia.com/terms/r/rsi.asp
    """

    def __init__(self) -> None:
        self.alpha = 2.0 / (14.0 + 1.0)

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        close_prev = state.get("close", current["close"])
        pct_change = (current["close"] - close_prev) / close_prev

        gain = pct_change if pct_change > 0 else 0.0
        loss = -1.0 * pct_change if pct_change < 0 else 0.0

        gain_ma = exponential_moving_average(
            self.alpha, gain, state.get("gain_ma", gain)
        )
        loss_ma = exponential_moving_average(
            self.alpha, loss, state.get("loss_ma", gain)
        )

        if loss_ma > 0:
            rsi = 100.0 - (100.0 / (1.0 + gain_ma / loss_ma))
        else:
            rsi = 100.0
        current.update(
            {
                "pct_change": pct_change,
                "gain_ma": gain_ma,
                "loss_ma": loss_ma,
                "rsi": rsi,
            }
        )
        return current, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Calculate RSI", self.builder, self.mapper)


class MA:
    """Moving average."""

    def __init__(self, window: int) -> None:
        """Constructor.

        Args:
            window - controls the window of average.
        """
        self.window = window
        self.name = f"moving_average_{window}"
        self.alpha = 2.0 / (window + 1.0)

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        c_ma = exponential_moving_average(
            self.alpha, current["close"], state.get(self.name, current["close"])
        )
        current.update({self.name: c_ma})
        return {self.name: c_ma}, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map(
            f"Calculate Moving Average {self.window}", self.builder, self.mapper
        )


class MFI:
    """Money Flow Index.

    https://www.investopedia.com/terms/m/mfi.asp
    """

    def __init__(self) -> None:
        self.alpha = 2.0 / (14.0 + 1.0)

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        typical_price = (current["close"] + current["high"] + current["low"]) / 3.0
        raw_money_flow = typical_price * current["volume"]

        typical_price_prev = state.get("typical_price", typical_price)
        positive_money_flow = (
            raw_money_flow if typical_price > typical_price_prev else 0.0
        )
        negative_money_flow = (
            raw_money_flow if typical_price < typical_price_prev else 0.0
        )

        positive_money_flow_ma = exponential_moving_average(
            self.alpha,
            positive_money_flow,
            state.get("positive_money_flow_ma", positive_money_flow),
        )

        negative_money_flow_ma = exponential_moving_average(
            self.alpha,
            negative_money_flow,
            state.get("negative_money_flow_ma", negative_money_flow),
        )

        if negative_money_flow_ma > 0:
            money_flow_ratio = positive_money_flow_ma / negative_money_flow_ma
        else:
            money_flow_ratio = 10000.0

        money_flow_index = 100.0 - (100.0 / (1 + money_flow_ratio))

        current.update(
            {
                "money_flow_index": money_flow_index,
                "mfi_delta": money_flow_index
                - state.get("money_flow_index", money_flow_index),
            }
        )

        state.update(
            {
                "typical_price": typical_price,
                "positive_money_flow_ma": positive_money_flow_ma,
                "negative_money_flow_ma": negative_money_flow_ma,
                "money_flow_index": money_flow_index,
            }
        )

        return state, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Money Flow Index", self.builder, self.mapper)


class SwingLow:
    """Swing Low.

    https://www.investopedia.com/terms/s/swinglow.asp
    """

    def __init__(self):
        self.period = 20

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        if "closes" not in state:
            state["closes"] = []
        state["closes"].append(current["close"])
        swing_low = min(state["closes"])

        current.update({"swing_low": swing_low})

        return {"closes": state["closes"][-self.period :]}, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Swing Low", self.builder, self.mapper)


class CoppockCurve:
    """Coppock Curve.

    https://www.investopedia.com/terms/c/coppockcurve.asp
    """

    def __init__(self):
        self.roc_long_period = 14 * 22  # 14 monthes, 22 woring days in month
        self.roc_short_period = 10 * 22  # 10 monthes
        self.wma_period = 10 * 22  # 10 monthes
        self.alpha = 2.0 / (self.wma_period + 1.0)

    @staticmethod
    def builder() -> State:
        return {}

    def mapper(self, state: State, current: KV) -> Tuple[KV, KV]:
        if "closes" not in state:
            state["closes"] = []

        closes = state["closes"][-self.roc_long_period :]
        closes.append(current["close"])

        if len(closes) < self.roc_long_period:
            roc_long = 0.0
            roc_short = 0.0
        else:
            roc_long = 100.0 * (
                (current["close"] - closes[-self.roc_long_period])
                / (closes[-self.roc_long_period])
            )

            roc_short = 100.0 * (
                (current["close"] - closes[-self.roc_short_period])
                / (closes[-self.roc_short_period])
            )

        roc = roc_long + roc_short
        coppock_curve = exponential_moving_average(
            self.alpha, roc, state.get("coppock_curve", roc)
        )

        current.update({"coppock_curve": coppock_curve})
        state.update({"coppock_curve": coppock_curve, "closes": closes})

        return state, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Coppock Curve", self.builder, self.mapper)
