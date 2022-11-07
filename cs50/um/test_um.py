from um import count


def test_correct():
    assert count("This is um, extreme sport") == 1

def test_wrong():
    assert count("...circumstances may differ") == 0

def test_punctuation():
    assert count("um, um... UM!") == 3