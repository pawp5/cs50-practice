from response import is_valid
import pytest

def test_correct():
    assert is_valid("henschel@gmail.com") == True

