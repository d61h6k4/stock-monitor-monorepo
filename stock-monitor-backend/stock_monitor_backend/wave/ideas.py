from h2o_lightwave import Q, ui
from stock_monitor_data import ideas

from stock_monitor_backend.wave.common import color_stock_dataframe, dataframe_to_data, preprocess_dataframe

_CARD_REGISTER = []


def idea_stock_graph(stock, box='1 3 11 5'):
    assert not stock.history.empty, stock.ticker_name

    y_min = stock.history["Low"].min() * 0.95
    y_max = stock.history["High"].max() * 1.05
    graph_data = dataframe_to_data(
        color_stock_dataframe(
            preprocess_dataframe(stock.history))[
            ["Date", "Low", "High", "Open", "Close", "Color", "Volume"]])

    return ui.form_card(
        box=box,
        items=[
            ui.text_xl(stock.ticker_name),
            ui.visualization(
                name='stock',
                height="260px",
                data=graph_data,
                plot=ui.plot(
                    [ui.mark(type='schema',
                             x_scale='time',
                             x='=Date',
                             y_q1="={{intl Open notation='compact' compactDisplay='short'}}",
                             y_q2="={{intl Open notation='compact' compactDisplay='short'}}",
                             y_q3="={{intl Close notation='compact' compactDisplay='short'}}",
                             y1="={{intl Low notation='compact' compactDisplay='short'}}",
                             y2="={{intl High notation='compact' compactDisplay='short'}}",
                             y_min=y_min,
                             y_max=max(y_max, stock.expectation.price * 1.05),
                             color="=Color",
                             color_range="#06982d #ae1325",
                             color_domain=["green", "red"]),
                     ui.mark(y=stock.expectation.price, label=f"Expected price {stock.expectation.price}", )])),
            ui.visualization(
                name='volume',
                height="100px",
                data=graph_data,
                plot=ui.plot(
                    [ui.mark(type='interval', x_scale='time', x='=Date',
                             y_scale="quantile",
                             y="={{intl Volume notation='compact' compactDisplay='short'}}",
                             color="=Color",
                             y_nice=True,
                             color_range="#06982d #ae1325",
                             color_domain=["green", "red"])
                     ])),
        ]
    )


async def render(q: Q):
    for ix, stock in enumerate(ideas(period="6mo", interval="1d")):
        graph = idea_stock_graph(stock, box=f"1 {2 + 6 * ix} 11 6")
        graph.items.append(ui.text_s(stock.description))
        q.page[f"stock_graph_{ix}"] = graph
        _CARD_REGISTER.append(f"stock_graph_{ix}")
