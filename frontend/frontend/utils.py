import re

ESCAPE_CHARS = re.escape(r"!$'")


def escape_markdown(txt: str) -> str:
    return re.sub(f"([{ESCAPE_CHARS}])", r"\\\1", txt) 
