import requests
import json

from tqdm import tqdm
from stock_monitor_data.data import ideas, portfolio, oil_and_gas_stocks, crypto, vix_stocks, etfs

_BOT_URL = "https://lochaufwallstrasse.de/bot/conversations/dbihbka/trigger_intent?output_channel=callback"


def watch(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_watchlist_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 43200
                                                 }}))
    r.raise_for_status()


def unwatch(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_unwatchlist_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 43200
                                                 }}))
    r.raise_for_status()


def monitor(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_asr_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 3600
                                                 }}))

    r.raise_for_status()


def main():
    # for idea in tqdm(ideas(period="3mo", interval="1d"), desc="Processing ideas..."):
    #     watch(idea)

    for stock in tqdm(portfolio(period="3mo", interval="1d"), desc="Processing portfolio..."):
        monitor(stock)

    # for stock in tqdm(oil_and_gas_stocks(period="3mo", interval="1d"), desc="Processing Oil&Gas..."):
    #     watch(stock)
    #
    # for stock in tqdm(crypto(period="3mo", interval="1d"), desc="Processing Crypto..."):
    #     watch(stock)
    #
    # for stock in tqdm(vix_stocks(period="3mo", interval="1d"), desc="Processing VIX..."):
    #     watch(stock)
    #
    # for stock in tqdm(etfs(period="3mo", interval="1d"), desc="Processing VIX..."):
    #     watch(stock)


if __name__ == "__main__":
    main()
