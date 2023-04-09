import pytest

from stock_monitor_backend.notifyer import NotificationCenter
from stock_monitor_backend.rules import Action, Decision, Rule
from stock_monitor_backend.utils import telegramify


class ClientMock:
    def __init__(self) -> None:
        self.messages = []

    def send_message(self, chat_id, text):
        self.messages.append({"chat_id": chat_id, "text": text})


@pytest.fixture()
def client_mock() -> ClientMock:
    return ClientMock()


@pytest.fixture()
def notifyer_mock() -> NotificationCenter:
    notifyer = NotificationCenter()
    return notifyer


def test_sends_message(notifyer_mock: NotificationCenter, client_mock: ClientMock):
    notifyer_mock.add_telegram(client_mock)

    decision = Decision(ticker="GOOG",
                        rule=Rule(name="rule1", description="Test rule"),
                        action=Action.HOLD,
                        explanation="Test")
    text = telegramify(decision)
    notifyer_mock.send_unique_decision("dbihbka", decision)

    assert client_mock.messages[0]["text"] == text


def test_donot_sends_duplicate_message(notifyer_mock: NotificationCenter, client_mock: ClientMock):
    notifyer_mock.add_telegram(client_mock)

    decision = Decision(ticker="GOOG",
                        rule=Rule(name="rule1", description="Test rule"),
                        action=Action.HOLD,
                        explanation="Test")
    telegramify(decision)
    notifyer_mock.send_unique_decision("dbihbka", decision)
    notifyer_mock.send_unique_decision("dbihbka", decision)

    assert len(client_mock.messages) == 1


def test_sends_different_message(notifyer_mock: NotificationCenter, client_mock: ClientMock):
    notifyer_mock.add_telegram(client_mock)

    decision = Decision(ticker="GOOG",
                        rule=Rule(name="rule1", description="Test rule"),
                        action=Action.HOLD,
                        explanation="Test")

    notifyer_mock.send_unique_decision("dbihbka", decision)

    decision.action = Action.BUY
    notifyer_mock.send_unique_decision("dbihbka", decision)
    text = telegramify(decision)

    assert len(client_mock.messages) == 2
    assert client_mock.messages[1]["text"] == text
