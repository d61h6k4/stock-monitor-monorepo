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
