from textwrap import dedent
from stock_monitor_backend.rules import Decision, Action


def emojify(a: Action) -> str:
    match a:
        case Action.SELL:
            return f"**sell** \U0001F4C9"
        case Action.HOLD:
            return "hold"
        case Action.BUY:
            return "buy \U0001F4C8"


def telegram_escape(text: str) -> str:
    for sym in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '}', '{', '.', '!']:
        text = text.replace(sym, f"\\{sym}")

    return text


def telegramify(decision: Decision) -> str:
    template = f"""
    **${decision.ticker} {emojify(decision.action)} \U000027A1 by {decision.rule.name}**
    ||{telegram_escape(decision.explanation)}||
    _{telegram_escape(decision.rule.description)}_
    #robotsopinion
    """

    return dedent(template)
