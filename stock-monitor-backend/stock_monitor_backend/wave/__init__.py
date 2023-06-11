from h2o_lightwave import Q, handle_on, on, ui

from stock_monitor_backend.wave import cot, report, portfolio, ideas

_CARD_REGISTER = {
    "cot": ["form", "stock_graph", "cot_net"],
    "report": ["form", "stock_graph", "rules_graph"],
    "portfolio": ["weights_graph"],
    "ideas": [],
    "about": [],
    None: []
}


async def clean_tab(q: Q):
    for card in _CARD_REGISTER[q.client.tab]:
        del q.page[card]


@on("#about")
async def on_about(q: Q):
    print("ABOUT")
    print(q.args)
    q.client.tab = "about"


@on("#report")
async def on_report(q: Q):
    if q.client.tab != "report":
        await clean_tab(q)
    q.client.tab = "report"

    await report.render(q)
    await q.page.save()


@on("#cot")
async def on_cot(q: Q):
    if q.client.tab != "cot":
        await clean_tab(q)
    q.client.tab = "cot"

    await cot.render(q)
    await q.page.save()


@on("#portfolio")
async def on_portfolio(q: Q):
    if q.client.tab != "portfolio":
        await clean_tab(q)
    q.client.tab = "portfolio"

    await portfolio.render(q)
    await q.page.save()


@on("#ideas")
async def on_ideas(q: Q):
    if q.client.tab != "ideas":
        await clean_tab(q)
    q.client.tab = "ideas"

    await ideas.render(q)
    await q.page.save()


# Lig callback function.
async def serve(q: Q):
    q.page['header'] = ui.header_card(
        box='1 1 -1 1',
        title='LAW',
        subtitle='Loch Auf Wallstrasse',
        icon='Money',
        nav=[
            ui.nav_group('Menu', items=[
                ui.nav_item(name="#report", label="Report"),
                ui.nav_item(name='#cot', label='COT'),
                ui.nav_item(name='#portfolio', label='Portfolio'),
                ui.nav_item(name='#ideas', label='Ideas'),
            ]),
            ui.nav_group('Help', items=[
                ui.nav_item(name='#about', label='About'),
                ui.nav_item(name='#support', label='Support'),
            ])
        ],
        color="card"
    )

    await handle_on(q)
    # Send the UI changes to the browser.
    await q.page.save()
