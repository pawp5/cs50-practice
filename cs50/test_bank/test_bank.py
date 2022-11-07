from bank import value


def test_hello():
    assert value("Hello there") == 0

def test_h():
    assert value("Hey, how's it going") == 20

def test_not_h():
    assert value("What's up?") == 100