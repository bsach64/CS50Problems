import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    if re.search(pattern, ip):
        numbers = ip.split(".")
        check = 1
        for number in numbers:
            if int(number) <= 255:
                check *= 1
            else:
                check *= 0
        if check == 1:
            return True
        else:
            return False
    return False


...


if __name__ == "__main__":
    main()