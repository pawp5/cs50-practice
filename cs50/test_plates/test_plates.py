from plates import is_valid


def test_min_len():
    assert is_valid("CS") == True
    assert is_valid("C") == False

def test_max_len():
    assert is_valid("ENYI11") == True
    assert is_valid("HENSCHEL") == False

def test_alpha_min():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False
    assert is_valid("CSE50") == True

def test_all_letters():
    assert is_valid("SOMMIE") == True
    assert is_valid("PRIDE") == True

def test_number_placement():
    assert is_valid("PE4ALL") == False
    assert is_valid("ENYI1") == True
    assert is_valid("ENYI01") == False

def test_punctuation():
    assert is_valid("ENYI 1") == False
    assert is_valid("ENYI.1") == False
    assert is_valid("ENYI,1") == False
    assert is_valid("ENYI#1") == False