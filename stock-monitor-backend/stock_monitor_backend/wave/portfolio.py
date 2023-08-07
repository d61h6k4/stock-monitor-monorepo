from h2o_lightwave import Q, data, ui

from stock_monitor_backend.position_sizing import get_weights


def bl_weights_graph():
    _, bl_weights = get_weights()
    weights = sorted([(k, v * 100) for k, v in bl_weights.items()], key=lambda x: x[1])

    return ui.plot_card(
        box="1 7 11 5",
        title="Black-Litterman model weights",
        data=data("ticker weight", len(weights), rows=weights),
        plot=ui.plot([ui.mark(type="interval", x="=weight", y="=ticker", y_min=0, y_nice=True)])
    )


def weights_graph():
    ef_weights, _ = get_weights()
    weights = sorted([(k, max(0, v) * 100) for k, v in ef_weights.items()], key=lambda x: x[1])

    return ui.plot_card(
        box="1 2 11 5",
        title="Portfolio weights (min volatility)",
        data=data("ticker weight", len(weights), rows=weights),
        plot=ui.plot([ui.mark(type="interval", x="=weight", y="=ticker", y_min=0, y_nice=True)])
    )


_CARD_REGISTER = ["weights_graph", "bl_weights_graph"]


async def render(q: Q):
    q.page["weights_graph"] = weights_graph()
    q.page["bl_weights_graph"] = bl_weights_graph()
