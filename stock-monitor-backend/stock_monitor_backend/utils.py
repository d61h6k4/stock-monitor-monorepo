from stock_monitor_backend.rules import Decision, Action


def emojify(a: Action) -> str:
    match a:
        case Action.SELL:
            return f"sell \U0001F4C9"
        case Action.HOLD:
            return "hold"
        case Action.BUY:
            return "buy \U0001F4C8"


def telegramify(decision: Decision) -> str:
    description = decision.rule.description.replace('.', ',')
    explanation = decision.explanation.replace('.', ',')
    return (f"Rule {decision.rule.name} \U000027A1 {emojify(decision.action)}.\n\n"
            f"<sup>{explanation}</sup>"
            f"<sup><sub>{description}</sub></sup>")
