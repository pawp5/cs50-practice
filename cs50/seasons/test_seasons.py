from seasons import minutes, format
from datetime import date, timedelta
import pytest


def test_correct_format():
    assert format("1999-07-28") == date(1999, 7, 28)

def test_invalid_format():
    with pytest.raises(SystemExit):
        assert format("1999/07/28")
    with pytest.raises(SystemExit):
        assert format("28 July, 1999")

def test_incorrect_format():
    for i in ["1000-13-28", "2001-09-32"]:
        with pytest.raises(SystemExit):
            assert format(i)
def test_correct_minutes():
    assert minutes(date(1999, 9, 9)) == 12029760