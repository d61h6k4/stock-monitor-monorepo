import pandas as pd
from h2o_lightwave import Q, data, ui

from stock_monitor_backend.models import Stock
from stock_monitor_backend.math import adx, rsi, macd


def preprocess_dataframe(df):
    new_df = df.reset_index()
    new_df["Date"] = new_df["Date"].apply(lambda el: el.isoformat(timespec="minutes"))

    return new_df


def color_stock_dataframe(df):
    df["Color"] = df[["Open", "Close"]].apply(lambda el: "green" if el["Open"] < el["Close"] else "red",
                                              axis=1)
    return df


def dataframe_to_data(df):
    return data(df.columns.to_list(), df.shape[0], rows=df.values.tolist(), pack=True)


def stock_graph(stock):
    graph_data = dataframe_to_data(
        color_stock_dataframe(
            preprocess_dataframe(stock.history))[
            ["Date", "Low", "High", "Open", "Close", "Color", "Volume"]])
    return ui.form_card(
        box='1 3 11 5',
        items=[
            ui.text_xl(stock.ticker_name),
            ui.visualization(
                name='stock',
                height="260px",
                data=graph_data,
                plot=ui.plot(
                    [ui.mark(type='schema', x_scale='time', x='=Date', y_q1="=Open", y_q2="=Open", y_q3='=Close',
                             y1="=Low",
                             y2="=High", y_nice=True, color="=Color", color_range="#06982d #ae1325",
                             color_domain=["green", "red"])])), ui.visualization(
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
                     ]))
        ]
    )


def rules_graph(stock):
    adx_df = preprocess_dataframe(adx(stock.history).stack()).rename(columns={"level_1": "kind", 0: "value"})
    adx_data = dataframe_to_data(adx_df)

    rsi_df = preprocess_dataframe(rsi(stock.history))
    rsi_data = dataframe_to_data(rsi_df)

    macd_line = macd(stock.history)
    signal_line = macd_line.ewm(alpha=1. / 9.).mean()
    macd_df = preprocess_dataframe(pd.concat([macd_line, signal_line], keys=["macd", "signal"])
                                   .reset_index()
                                   .rename(columns={"level_0": "kind"})
                                   .set_index("Date"))

    macd_data = dataframe_to_data(macd_df)

    return ui.form_card(
        box="1 8 11 5",
        items=[
            ui.text_m("ADX"),
            ui.visualization(
                name="ADX",
                height="150px",
                data=adx_data,
                plot=ui.plot([
                    ui.mark(type="line",
                            x="=Date",
                            y="=value",
                            x_scale="time",
                            y_nice=True,
                            color="=kind",
                            color_range="#06982d #ae1325 #008FD3",
                            color_domain=["+di", "-di", "adx"]),
                ])),
            ui.text_m("RSI"),
            ui.visualization(
                name="RSI",
                height="150px",
                data=rsi_data,
                plot=ui.plot([
                    ui.mark(type="line",
                            x="=Date",
                            y="=Close",
                            x_scale="time",
                            y_nice=True,
                            color="#008FD3")
                ])),
            ui.text_m("MACD"),
            ui.visualization(
                name="MACD",
                height="150px",
                data=macd_data,
                plot=ui.plot([
                    ui.mark(type="line",
                            x="=Date",
                            y="=Close",
                            x_scale="time",
                            y_nice=True,
                            color="=kind",
                            color_range="#06982d #ae1325",
                            color_domain=["macd", "signal"])
                ]))
        ]
    )


async def render(q: Q):
    q.page['form'] = ui.form_card(
        box='1 2 11 1',
        items=[ui.inline(height="40px",
                         items=[
                             ui.label(label='Ticker'),
                             ui.textbox(name='ticker'),
                             ui.button(name="stock_form_ready", label="Show"),
                         ])],
    )

    if q.args.stock_form_ready:
        stock = Stock(ticker_name=q.args.ticker, period="6mo", interval="1d")

        q.page["stock_graph"] = stock_graph(stock)
        q.page["rules_graph"] = rules_graph(stock)
