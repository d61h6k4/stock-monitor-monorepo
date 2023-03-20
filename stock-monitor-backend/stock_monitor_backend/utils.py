from stock_monitor_backend.rules import Decision, Action


def emojify(a: Action) -> str:
    match a:
        case Action.SELL:
            return f"**sell** \U0001F4C9"
        case Action.HOLD:
            return "hold"
        case Action.BUY:
            return "buy \U0001F4C8"


def telegramify(decision: Decision) -> str:
    template = f"""
    ${decision.ticker} {emojify(decision.action)} \U000027A1 by {decision.rule.name}


    ##### {decision.explanation}


    ###### {decision.rule.description}
    """
    for sym in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '}', '{', '.', '!']:
        template = template.repalce(sym, f"\\{sym}")
    return template
