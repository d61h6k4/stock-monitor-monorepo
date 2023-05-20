import pandas as pd
from h2o_lightwave import Q, data, ui

from stock_monitor_backend.models import Stock
from stock_monitor_backend.math import adx, rsi, macd

from stock_monitor_backend.wave.common import preprocess_dataframe, dataframe_to_data, stock_graph


def rules_graph(stock):
    adx_df = preprocess_dataframe(adx(stock.history).stack()).rename(columns={"level_1": "kind", 0: "value"})
    adx_data = dataframe_to_data(adx_df)

    rsi_df = preprocess_dataframe(
        rsi(stock.history).to_frame(name="rsi")
        .assign(buy=lambda _: 30.0, sell=lambda _: 70.0)
        .stack()).rename(columns={"level_1": "kind", 0: "value"})
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
            ui.text_s("""The ADX, negative directional indicator (-DI), and positive directional indicator (+DI)
                         are momentum indicators. The ADX helps investors determine trend strength,
                         while -DI and +DI help determine trend direction. The ADX identifies a strong trend when
                         the ADX is over 25 and a weak trend when the ADX is below 20."""),
            ui.text_m("RSI"),
            ui.visualization(
                name="RSI",
                height="150px",
                data=rsi_data,
                plot=ui.plot([
                    ui.mark(type="line",
                            x="=Date",
                            y="=value",
                            x_scale="time",
                            y_nice=True,
                            color="=kind",
                            color_range="#06982d #ae1325 #008FD3",
                            color_domain=["buy", "sell", "rsi"])
                ])),
            ui.text_s("""RSI values of 70 or above indicate that a security is becoming overbought or overvalued.
                         An RSI reading of 30 or below indicates an oversold or undervalued condition."""),
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
                ])),
            ui.text_s("""The MACD line is calculated by subtracting the 26-period EMA from the 12-period EMA.
                         The result of that calculation is the MACD line. A nine-day EMA of the MACD line is
                         called the signal line, which is then plotted on top of the MACD line, which can
                         function as a trigger for buy or sell signals. Traders may buy the security when the
                         MACD line crosses above the signal line and sell—or short—the security when the MACD
                         line crosses below the signal line."""),
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
