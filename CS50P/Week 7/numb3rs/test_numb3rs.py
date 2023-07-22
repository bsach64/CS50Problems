from numb3rs import validate

def main():
    test_numb3rs()

def test_numb3rs():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("225.258.270.245") == False

if __name__ == "__main__":
    main()