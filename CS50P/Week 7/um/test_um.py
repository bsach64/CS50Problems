from um import count

def main():
    test_count()

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...")

if __name__ == "__main__":
    main()