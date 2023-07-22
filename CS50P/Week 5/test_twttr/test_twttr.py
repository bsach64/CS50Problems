from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("Vowel") == "Vwl"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("12,23#") == "12,23#"

if __name__ == "__main__":
    main()