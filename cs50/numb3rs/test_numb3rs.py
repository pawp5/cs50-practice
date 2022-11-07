from numb3rs import validate

def test_min():
    assert validate("0.0.0.0") == True

def test_max():
    assert validate("255.255.255.255") == True

def test_256():
    assert validate("256.255.255.255") == False

def test_first_byte():
    assert validate("17.600.43.56") == False

def test_incomplete():
    assert validate("23.67.23.") == False
    assert validate("23.67.0") == False

def test_sentence():
    assert validate("Hello world") == False

def text_text():
    assert validate("23.67.2cat.45") == False
    assert validate("23.67.23.dawg") == False