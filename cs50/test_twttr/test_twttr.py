from twttr import shorten


def test_upper():
    assert shorten("BEAUTIFIL") == "BTFL"

def test_lower():
    assert shorten("beautiful") == "btfl"

def test_mixed():
    assert shorten("Beautiful") == "Btfl"
    assert shorten("BeAutIFul") == "BtFl"

def test_punctuations():
    assert shorten("Important.!?") == "mprtnt.!?"

def test_numbers():
    assert shorten("0123456789") == "0123456789"