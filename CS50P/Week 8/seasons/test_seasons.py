from seasons import validate_date
import pytest

def main():
    test_validate_date()

def test_validate_date():
    assert validate_date("2001-01-01") == True
    with pytest.raises(SystemExit):
        assert validate_date("February 6th, 1998")
        assert validate_date("2023-23-23")

if __name__ == "__main__":
    main()