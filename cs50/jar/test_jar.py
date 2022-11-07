from jar import Jar
import pytest

jar = Jar()
def test_init():
    assert jar.capacity == 12

def test_str():
    jar.deposit(7) # Depositing 7 cookies. Bal 7
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    assert jar.size == 7

    with pytest.raises(ValueError):
        assert jar.deposit(6) # Try to deposit 6 more cookies. ERROR

def test_withdraw():
    jar.withdraw(5) # Withdrawing 5 cookies. Bal 2
    assert jar.size == 2

    with pytest.raises(ValueError):
        assert jar.withdraw(5) # Try to withdraw 5 more cookies. ERROR