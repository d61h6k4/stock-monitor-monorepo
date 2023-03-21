from functools import wraps

from stock_monitor_backend.rules import Decision
from stock_monitor_backend.telegram.client import TelegramClient
from stock_monitor_backend.utils import telegramify

TELEGRAM = "telegram"


def is_user_exists(method):
    @wraps(method)
    def _impl(self, user, *args, **kwargs):
        if user not in self._users_to_chats:
            raise ValueError(f"Given user {user} is unknown.")
        return method(self, user, *args, **kwargs)

    return _impl


def is_client_exists(method):
    @wraps(method)
    def _impl(self, *args, **kwargs):
        if TELEGRAM not in self._clients:
            raise ValueError("Telegram client hasn't been registered in Notification center yet.")
        return method(self, *args, **kwargs)

    return _impl


class NotificationCenter:
    def __init__(self) -> None:
        self._clients = {}
        self._users_to_chats = {"dbihbka": 111874928}
        self._users_last_messages = {}

    def add_telegram(self, client: TelegramClient):
        self._clients[TELEGRAM] = client

    @is_client_exists
    @is_user_exists
    def send_unique_decision(self, user: str, decision: Decision):
        if user not in self._users_last_messages:
            self._users_last_messages[user] = {}
        if decision.ticker not in self._users_last_messages[user]:
            self._users_last_messages[user][decision.ticker] = None
        if self._users_last_messages[user][decision.ticker] != decision.action:
            text = telegramify(decision)
            self._clients[TELEGRAM].send_message(chat_id=self._users_to_chats[user],
                                                 text=text)

            self._users_last_messages[user][decision.ticker] = decision.action
