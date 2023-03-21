from functools import wraps

from stock_monitor_backend.rules import Decision
from stock_monitor_backend.telegram.client import TelegramClient
from stock_monitor_backend.utils import telegramify

TELEGRAM = "telegram"


def is_user_exists(method):
    @wraps(method)
    def _impl(self, user, *args, **kwargs):
        if user not in self.__users_to_chats:
            raise ValueError(f"Given user {user} is unknown.")
        return method(self, user, *args, **kwargs)

    return _impl


def is_client_exists(method):
    @wraps(method)
    def _impl(self, *args, **kwargs):
        if TELEGRAM not in self.__clients:
            raise ValueError("Telegram client hasn't been registered in Notification center yet.")
        return method(self, *args, **kwargs)

    return _impl


class NotificationCenter:
    def __init__(self) -> None:
        self.__clients = {}
        self.__users_to_chats = {"dbihbka": 111874928}
        self.__users_last_messages = {}

    def add_telegram(self, client: TelegramClient):
        self.__clients[TELEGRAM] = client

    @is_client_exists
    @is_user_exists
    def send_unique_decision(self, user: str, decision: Decision):
        if user not in self.__users_last_messages:
            self.__users_last_messages[user] = {}
        if decision.ticker not in self.__users_last_messages[user]:
            self.__users_last_messages[user][decision.ticker] = None
        if self.__users_last_messages[user][decision.ticker] != decision.action:
            text = telegramify(decision)
            self.__clients[TELEGRAM].send_message(chat_id=self.__users_to_chats[user],
                                                  text=text)

            self.__users_last_messages[user][decision.ticker] = decision.action
