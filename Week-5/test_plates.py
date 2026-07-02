from plates import is_valid

def test_length():
    assert is_valid("H") == False
    assert is_valid("ABCDEFG") == False

def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False

def test_zero():
    assert is_valid("CS05") == False

def test_symbols():
    assert is_valid("PI3.14") == False
