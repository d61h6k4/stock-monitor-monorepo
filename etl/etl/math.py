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
                "gain_ma": gain_ma,
                "loss_ma": loss_ma,
                "rsi": rsi,
            }
        )
        return current, current

    def __call__(self, flow: Dataflow):
        flow.stateful_map("Calculate RSI", self.builder, self.mapper)
