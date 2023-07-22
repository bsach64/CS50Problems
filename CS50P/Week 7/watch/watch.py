import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"src=\"https?\:\/\/(www\.)?youtube\.com\/embed\/(\w+)"
    matches = re.search(pattern, s)
    if matches:
        return ("https://youtu.be/" + matches.group(2))
    else:
        return None


if __name__ == "__main__":
    main()