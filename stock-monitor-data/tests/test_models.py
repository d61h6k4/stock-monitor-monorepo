from stock_monitor_data.models import Stock


def test_smoke_stock():
    s = Stock(ticker_name="U-UN.TO", period="3mo", interval="1d")

    assert s.industry is not None
    assert s.sector is not None
