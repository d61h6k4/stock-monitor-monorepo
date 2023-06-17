"""Sends notifications to the clients."""

import json
from pathlib import Path
from typing import Self

from stock_monitor_backend.rules import Action, Decision
from stock_monitor_backend.telegram.client import TelegramClient
from stock_monitor_backend.utils import telegramify

TELEGRAM = "telegram"


class NotificationCenter:
    """Sends notifications."""

    def __init__(self: Self) -> None:
        """Constructor."""
        self._clients = {}
        self._users_to_chats = {"dbihbka": 111874928}

        self._users_last_messages = {}
        self._resource = Path.home() / Path(".notifyer.json")
        if self._resource.exists():
            for user, values in json.loads(self._resource.read_text()).items():
                self._users_last_messages[user] = {}
                for ticker, t_values in values.items():
                    self._users_last_messages[user][ticker] = {}
                    for rule, state in t_values.items():
                        self._users_last_messages[user][ticker][rule] = Action.from_string(state)

    def add_telegram(self: Self, client: TelegramClient) -> None:
        """Add telegram as one of the channels to send notifications."""
        self._clients[TELEGRAM] = client

    def send_unique_decision(self: Self, user: str, decision: Decision) -> None:
        """Checks uniqness of the given decision and sends it to the user."""
        self.check_user_exists(user)
        self.check_client_exists(TELEGRAM)

        if user not in self._users_last_messages:
            self._users_last_messages[user] = {}
        if decision.ticker not in self._users_last_messages[user]:
            self._users_last_messages[user][decision.ticker] = {}
        if decision.rule.name not in self._users_last_messages[user][decision.ticker]:
            self._users_last_messages[user][decision.ticker][decision.rule.name] = None
        if self._users_last_messages[user][decision.ticker][decision.rule.name] != decision.action:
            text = telegramify(decision)
            self._clients[TELEGRAM].send_message(chat_id=self._users_to_chats[user],
                                                 text=text)

            self._users_last_messages[user][decision.ticker][decision.rule.name] = decision.action

    def check_user_exists(self: Self, user: str) -> None:
        """Checks the given `user` is known."""
        if user not in self._users_to_chats:
            err_msg = f"Given user {user} is unknown."
            raise ValueError(err_msg)

    def check_client_exists(self: Self, client: str) -> None:
        """Checks the given `client` is known."""
        if client not in self._clients:
            err_msg = "Telegram client hasn't been registered in Notification center yet."
            raise ValueError(err_msg)

    def persist(self) -> None:
        """Persist the data to the disk."""
        if self._resource.exists():
            self._resource.unlink()

        self._resource.write_text(json.dumps(self._users_last_messages))
