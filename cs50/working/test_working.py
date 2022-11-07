import pytest
from working import convert

def test_long():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_short():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_long_short():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_lower():
    with pytest.raises(ValueError):
        assert convert("9:00 am to 5:00 pm")

def test_12():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_min():
    assert convert("9:59 AM to 6:15 PM") == "09:59 to 18:15"

def test_range():
    with pytest.raises(ValueError):
        assert convert("13 AM to 4 PM")

def test_omit_to():
    with pytest.raises(ValueError):
        assert convert("5 AM - 12 PM")

def test_format():
    with pytest.raises(ValueError):
        assert convert("12.00 to 6.00")