from stock_monitor_backend.rules import Decision, Action


def emojify(a: Action) -> str:
    match a:
        case Action.SELL:
            return f"sell \\U+1F4C9"
        case Action.HOLD:
            return "hold"
        case Action.BUY:
            return "buy \\U+1F4C8"


def telegramify(decision: Decision) -> str:
    return (f"Rule {decision.rule.name} \\U+27A1 {emojify(decision.action)}.\n\n"
            f"<sup><sub>{decision.explanation}</sub></sup>")
