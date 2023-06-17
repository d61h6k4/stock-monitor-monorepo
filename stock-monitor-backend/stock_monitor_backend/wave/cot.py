from datetime import datetime

from h2o_lightwave import Q, ui
from stock_monitor_data.models import COT, Stock

from stock_monitor_backend.math import cot_index, cot_move_index, cot_net_position
from stock_monitor_backend.wave.common import dataframe_to_data, preprocess_dataframe, stock_graph


async def render(q: Q):
    if q.args.cot_form_reset_form:
        q.args.cot_form_since = None
        q.args.cot_form_names = None
        q.args.cot_form_codes = None
        q.args.cot_form_period = None
        q.args.cot_form_ticker = None
        q.args.cot_form_ready = False

    default_cot = COT(since=datetime.today().year)
    q.page["form"] = ui.form_card(box="1 2 3 5",
                                  title="Commitment of Traders",
                                  items=[
                                      ui.date_picker(name="cot_form_since",
                                                     label="COT period",
                                                     placeholder="Since which year download COT data.",
                                                     value=(q.args.cot_form_since or str(
                                                         datetime.today().isoformat()))),
                                      ui.dropdown(name="cot_form_names", label="Market and exchange names", choices=[
                                          ui.choice(name=n.replace(' ', '_'), label=f"{n} (Code {c})")
                                          for n, c in
                                          set(tuple(x) for x in default_cot.history[["Market_and_Exchange_Names",
                                                                                     "CFTC_Commodity_Code"]].values)
                                      ], values=(q.args.cot_form_names or []), required=False),
                                      ui.dropdown(name="cot_form_codes", label="Market and exchange names by code",
                                                  choices=[
                                                      ui.choice(name=str(c), label=f"{n} (Code {c})")
                                                      for n, c in
                                                      set(tuple(x) for x in
                                                          default_cot.history[["Market_and_Exchange_Names",
                                                                               "CFTC_Commodity_Code"]].values)
                                                  ], values=(q.args.cot_form_codes or []), required=False),
                                      ui.slider(name="cot_form_period", label="Rolling window size (weeks)", min=1,
                                                max=3 * 365 // 7, step=1, value=(q.args.cot_form_period or 26)),
                                      ui.textbox(name="cot_form_ticker", label="Stock ticker",
                                                 value=(q.args.cot_form_ticker or None)),
                                      ui.buttons(items=[
                                          ui.button(name="cot_form_ready", label="Show"),
                                          ui.button(name="cot_form_reset_form", label="Reset"),
                                      ]),
                                  ])

    if q.args.cot_form_ready:
        cot = COT(since=datetime.fromisoformat(q.args.cot_form_since).year)
        df = cot.commercials_by_names_or_codes(cot.history,
                                               names=[n.replace('_', ' ') for n in set(q.args.cot_form_names)],
                                               codes=[int(c) for c in set(q.args.cot_form_codes)])
        cdf = cot_index(df, q.args.cot_form_period).to_frame(name="cot_index") \
            .join(cot_move_index(df, q.args.cot_form_period).to_frame(name="cot_move_index")) \
            .join(cot_net_position(df).to_frame(name="net")) \
            .dropna()
        if q.args.cot_form_ticker:
            stock_df = Stock(ticker_name=q.args.cot_form_ticker, period="5y", interval="1wk")
            cdf = cdf.join(stock_df.history.to_period("w")).to_timestamp().reset_index().fillna(0.0)

            stock_df.history = cdf.rename(columns={"Report_Date_as_MM_DD_YYYY": "Date"}).set_index("Date")
            q.page["stock_graph"] = stock_graph(stock_df, box="4 2 -1 5")
            cot_chart_start = 7
        else:
            cdf = cdf.to_timestamp().reset_index()
            cot_chart_start = 2

        cot_net_data = dataframe_to_data(
            preprocess_dataframe(cdf.rename(columns={"Report_Date_as_MM_DD_YYYY": "Date"})
                                 [["Date", "net", "cot_index", "cot_move_index"]]
                                 .set_index("Date")))
        q.page["cot_net"] = ui.form_card(box=f"4 {cot_chart_start} -1 6",
                                         items=[
                                             ui.text_l("Commercial Net position"),
                                             ui.visualization(name="cot_net",
                                                              data=cot_net_data,
                                                              height="120px",
                                                              plot=ui.plot([
                                                                  ui.mark(type="interval", x_scale='time',
                                                                          x='=Date',
                                                                          y="={{intl net notation='compact' compactDisplay='short'}}",
                                                                          y_nice=True,
                                                                          color="#06982d")
                                                              ])),
                                             ui.text_l("COT Index"),
                                             ui.visualization(name="cot_index",
                                                              data=cot_net_data,
                                                              height="120px",
                                                              plot=ui.plot([
                                                                  ui.mark(type="interval", x_scale='time',
                                                                          x='=Date',
                                                                          y_scale="quantile",
                                                                          y="={{intl cot_index notation='compact' compactDisplay='short'}}",
                                                                          y_nice=True,
                                                                          color="#06982d")
                                                              ])),
                                             ui.text_l("COT Move Index"),
                                             ui.visualization(name="cot_move_index",
                                                              data=cot_net_data,
                                                              height="120px",
                                                              plot=ui.plot([
                                                                  ui.mark(type="interval", x_scale='time',
                                                                          x='=Date',
                                                                          y="={{intl cot_move_index notation='compact' compactDisplay='short'}}",
                                                                          y_nice=True,
                                                                          color="#06982d")
                                                              ])),

                                         ])
