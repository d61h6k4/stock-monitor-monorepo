from frontend.utils import escape_markdown


def test_escape_markdown():
    assert (
        escape_markdown(
            "Google's last price is $120[Source](https://mcusercontent.com/)"
        )
        == "Google\\'s last price is \\$120[Source](https://mcusercontent.com/)"
    )
