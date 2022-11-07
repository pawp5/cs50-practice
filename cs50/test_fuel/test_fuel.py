from fuel import convert, gauge
import pytest

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("4/2")

def test_convert_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convert_fraction():
    assert convert("5/8") == 62

def test_gauge_full_empty():
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_gauge_numbers():
    assert gauge(7) == "7%"
    assert gauge(82) == "82%"