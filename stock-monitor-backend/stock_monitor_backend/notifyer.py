"""Sends notifications to the clients."""

from stock_monitor_backend.rules import Decision
from stock_monitor_backend.telegram.client import TelegramClient
from stock_monitor_backend.utils import telegramify

TELEGRAM = "telegram"


class NotificationCenter:
    def __init__(self) -> None:
        self._clients = {}
        self._users_to_chats = {"dbihbka": 111874928}
        self._users_last_messages = {}

    def add_telegram(self, client: TelegramClient):
        self._clients[TELEGRAM] = client

    def send_unique_decision(self, user: str, decision: Decision):
        self.check_user_exists(user)
        self.check_client_exists(TELEGRAM)

        if user not in self._users_last_messages:
            self._users_last_messages[user] = {}
        if decision.ticker not in self._users_last_messages[user]:
            self._users_last_messages[user][decision.ticker] = None
        if self._users_last_messages[user][decision.ticker] != decision.action:
            text = telegramify(decision)
            self._clients[TELEGRAM].send_message(chat_id=self._users_to_chats[user],
                                                 text=text)

            self._users_last_messages[user][decision.ticker] = decision.action

    def check_user_exists(self, user: str):
        if user not in self._users_to_chats:
            raise ValueError(f"Given user {user} is unknown.")

    def check_client_exists(self, client: str):
        if client not in self._clients:
            raise ValueError("Telegram client hasn't been registered in Notification center yet.")
