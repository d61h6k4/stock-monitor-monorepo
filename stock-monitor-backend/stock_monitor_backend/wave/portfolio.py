from h2o_lightwave import Q, ui, data
from stock_monitor_backend.position_sizing import get_weights


def weights_graph():
    weights = sorted([(k, v * 100) for k, v in get_weights().items()], key=lambda x: x[1])

    return ui.plot_card(
        box="1 2 11 5",
        title="Portfolio weights",
        data=data("ticker weight", len(weights), rows=weights),
        plot=ui.plot([ui.mark(type="interval", x="=weight", y="=ticker", y_min=0, y_nice=True)])
    )


async def render(q: Q):
    q.page["weights_graph"] = weights_graph()
