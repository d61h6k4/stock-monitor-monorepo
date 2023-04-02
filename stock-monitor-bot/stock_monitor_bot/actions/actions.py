# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from structlog import get_logger
from typing import Sequence
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, ReminderCancelled, ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

LOGGER = get_logger()


def get_ticker(tracker: Tracker) -> str:
    """Extracts entity tricker value from the tracker."""
    ticker = next(tracker.get_latest_entity_values("ticker"))
    assert ticker, f"Expected to get 1 ticker but {ticker}"
    return ticker


def get_seconds(tracker: Tracker) -> float:
    """Extract value of the timedelta entity."""
    seconds = next(tracker.get_latest_entity_values("seconds"), "1")
    return float(seconds)


def create_asr_reminder_name(ticker: str) -> str:
    """Creates a name of an ASR reminder event."""
    return f"asr_reminder_for_{ticker}"


def create_asr_reminder(ticker: str, seconds: float) -> ReminderScheduled:
    """Creates an asr reminder event."""
    return ReminderScheduled("asr_reminder",
                             trigger_date_time=datetime.now() + timedelta(seconds=float(seconds)),
                             entities=[{"entity": "ticker", "value": ticker},
                                       {"entity": "seconds", "value": seconds}],
                             name=create_asr_reminder_name(ticker),
                             kill_on_user_message=False,
                             )


def create_watchlist_reminder_name(ticker: str) -> str:
    """Creates a name of an WatchList reminder event."""
    return f"watchlist_reminder_for_{ticker}"


def create_watchlist_reminder(ticker: str, seconds: float) -> ReminderScheduled:
    """Creates an watch list reminder event."""
    return ReminderScheduled("watchlist_reminder",
                             trigger_date_time=datetime.now() + timedelta(seconds=float(seconds)),
                             entities=[{"entity": "ticker", "value": ticker},
                                       {"entity": "seconds", "value": seconds}],
                             name=create_watchlist_reminder_name(ticker),
                             kill_on_user_message=False,
                             )


class ActionSetASRReminder(Action):
    """Schedules a reminder of checking the `ticker` in `timedelta` minutes."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_set_asr_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)
        seconds = get_seconds(tracker)

        LOGGER.info({"name": self.name(),
                     "entities": {"ticker": ticker,
                                  "seconds": seconds}})

        return [create_asr_reminder(ticker, seconds)]


class ActionReactToASRReminder(Action):
    """Checks ASR sell rule for the given ticker and resets reminder."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_react_to_asr_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)
        seconds = get_seconds(tracker)

        dispatcher.utter_message(
            json_message={"name": self.name(),
                          "entities": {"ticker": ticker,
                                       "seconds": seconds},
                          })
        return [create_asr_reminder(ticker, seconds)]


class ActionUnsetASRReminder(Action):
    """Removes ASR reminder."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_unset_asr_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)

        LOGGER.info({"name": self.name(),
                     "entities": {"ticker": ticker}})

        return [ReminderCancelled(name=create_asr_reminder_name(ticker))]


class ActionSetWatchListReminder(Action):
    """Schedules a reminder of checking the `ticker` in `timedelta` minutes."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_set_watchlist_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)
        seconds = get_seconds(tracker)

        LOGGER.info({"name": self.name(),
                     "entities": {"ticker": ticker,
                                  "seconds": seconds}})

        return [create_watchlist_reminder(ticker, seconds)]


class ActionReactToWatchListReminder(Action):
    """Checks Watch list sell rule for the given ticker and resets reminder."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_react_to_wathclist_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)
        seconds = get_seconds(tracker)

        dispatcher.utter_message(
            json_message={"name": self.name(),
                          "entities": {"ticker": ticker,
                                       "seconds": seconds},
                          })
        return [create_watchlist_reminder(ticker, seconds)]


class ActionUnsetWatchListReminder(Action):
    """Removes Watch list reminder."""

    def name(self) -> str:
        """Returns name of the action to use as a key to register."""
        return "action_unset_watchlist_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Sequence[EventType]:
        ticker = get_ticker(tracker)

        LOGGER.info({"name": self.name(),
                     "entities": {"ticker": ticker}})

        return [ReminderCancelled(name=create_watchlist_reminder_name(ticker))]
