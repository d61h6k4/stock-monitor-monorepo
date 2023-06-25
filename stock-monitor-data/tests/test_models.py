from stock_monitor_data.models import COT

def test_smoke_cot():
    cot = COT(since=2015)
    
    assert cot.history is not None