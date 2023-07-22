from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1 / 100") == 1
    assert convert("1 / 1000") == 0
    assert convert("1 / 2") == 50
    with pytest.raises(ZeroDivisionError):
        assert convert("1 / 0")
    with pytest.raises(ValueError):
        assert convert("x / y")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    
if __name__ == "__main__":
    main()