from h2o_lightwave import Q, ui
from stock_monitor_data.data import ideas
from stock_monitor_backend.wave.common import stock_graph


async def render(q: Q):
    for ix, stock in enumerate(ideas(period="6mo", interval="1d")):
        graph = stock_graph(stock, box=f"1 {2 + 6 * ix} 11 6")
        graph.items.append(ui.text_s(stock.description))
        q.page[f"stock_graph_{ix}"] = graph
