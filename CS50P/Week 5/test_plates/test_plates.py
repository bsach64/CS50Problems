from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("Hello") == True
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False