from textwrap import dedent
from stock_monitor_backend.rules import Decision, Action


def emojify(a: Action) -> str:
    match a:
        case Action.SELL:
            return f"\U0001F4C9 **sell** \U0001F4B8"
        case Action.HOLD:
            return "\U0001F7F0 **hold** \U0001F4B0"
        case Action.BUY:
            return "\U0001F4C8 **buy** \U0001F911"


def telegram_escape(text: str) -> str:
    for sym in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '}', '{', '.', '!']:
        text = text.replace(sym, f"\\{sym}")

    return text


def telegramify(decision: Decision) -> str:
    template = f"""
    **${decision.ticker} {emojify(decision.action)} \U000027A1 by {decision.rule.name}**
    ||{telegram_escape(decision.explanation)}||
    _{telegram_escape(decision.rule.description)}_
    \U0001F916 \\#robotsopinion
    """

    return dedent(template)
