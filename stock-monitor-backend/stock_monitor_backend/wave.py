from datetime import datetime

from altair import Y2, Axis, Chart, Scale, X, Y, condition, value
from h2o_lightwave import Q, handle_on, on, ui

from stock_monitor_backend.math import cot_index, cot_move_index, cot_net_position
from stock_monitor_backend.models import COT, Stock

_CARD_REGISTER = {
    "cot": ["form", "plot"],
    "about": [],
}


async def clean_tab(q: Q):
    for card in _CARD_REGISTER[q.client.tab]:
        del q.page[card]


@on("#cot")
async def on_cot(q: Q):
    if q.client.tab != "cot":
        await clean_tab(q)
        q.client.tab = "cot"

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

        open_close_color = condition("5 < datum.cot_index && datum.cot_index < 90",
                                     value("#06982d"),
                                     value("#ae1325"))
        if q.args.cot_form_ticker:
            stock_df = Stock(ticker_name=q.args.cot_form_ticker, period="5y", interval="1wk")
            cdf = cdf.join(stock_df.history.to_period("w")).to_timestamp().reset_index().fillna(0.0)

            base = Chart(cdf).encode(
                X("Report_Date_as_MM_DD_YYYY:T", axis=Axis(title=None)), color=open_close_color
            )

            rule = base.mark_rule().encode(
                Y(
                    'Low:Q',
                    title=f'{q.args.cot_form_ticker}',
                    scale=Scale(zero=False)
                ),
                Y2('High:Q')
            ) \
                .properties(width="container", height="container")

            bar = base.mark_bar().encode(
                Y('Open:Q'),
                Y2('Close:Q')
            ) \
                .properties(width="container", height="container")
            chart_spec = (rule + bar).to_json()
            q.page["cot_stock_chart"] = ui.vega_card(box="4 2 -1 4",
                                                     title="Stock",
                                                     specification=chart_spec)
            cot_chart_start = 4
        else:
            cdf = cdf.to_timestamp().reset_index()

            base = Chart(cdf).encode(
                X("Report_Date_as_MM_DD_YYYY:T", axis=Axis(title=None)), color=open_close_color
            )
            cot_chart_start = 0

        cot_net_chart = base.mark_bar() \
            .encode(x=X("Report_Date_as_MM_DD_YYYY:T", title="date", axis=Axis(title=None)),
                    y=Y("net:Q", title="COT net position", axis=Axis(title=None))) \
            .properties(width="container", height="container")

        cot_net_chart_spec = cot_net_chart \
            .to_json()
        q.page["cot_net_chart"] = ui.vega_card(box=f"4 {cot_chart_start + 2} -1 2",
                                               title="COT Net position (commercials)",
                                               specification=cot_net_chart_spec)
        cot_index_chart = base.mark_bar() \
            .encode(x=X("Report_Date_as_MM_DD_YYYY:T", title="date", axis=Axis(title=None)),
                    y=Y("cot_index:Q", title="COT index", axis=Axis(title=None))) \
            .properties(width="container", height="container")

        cot_index_chart_spec = cot_index_chart \
            .to_json()
        q.page["cot_index_chart"] = ui.vega_card(box=f"4 {cot_chart_start + 4} -1 2",
                                                 title="COT index",
                                                 specification=cot_index_chart_spec)
        cot_move_index_chart = base.mark_bar() \
            .encode(x=X("Report_Date_as_MM_DD_YYYY:T", title="date", axis=Axis(title=None)),
                    y=Y("cot_move_index:Q", title="COT index move", axis=Axis(title=None))) \
            .properties(width="container", height="container")

        cot_move_index_chart_spec = cot_move_index_chart \
            .to_json()
        q.page["cot_move_index_chart"] = ui.vega_card(box=f"4 {cot_chart_start + 6} -1 2",
                                                      title="COT index move",
                                                      specification=cot_move_index_chart_spec)

    await q.page.save()


@on("#about")
async def on_about(q: Q):
    print("ABOUT")
    print(q.args)
    q.client.tab = "about"


# Lig callback function.
async def serve(q: Q):
    q.page['header'] = ui.header_card(
        box='1 1 -1 1',
        title='LAW',
        subtitle='Loch Auf Wallstrasse',
        icon='Money',
        nav=[
            ui.nav_group('Menu', items=[
                ui.nav_item(name='#cot', label='COT'),
            ]),
            ui.nav_group('Help', items=[
                ui.nav_item(name='#about', label='About'),
                ui.nav_item(name='#support', label='Support'),
            ])
        ],
        color="card"
    )

    if not await handle_on(q):
        q.client.tab = "cot"
        await on_cot(q)

    # Send the UI changes to the browser.
    await q.page.save()
