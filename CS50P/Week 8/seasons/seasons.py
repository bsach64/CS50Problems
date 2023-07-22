from datetime import date
import re
import inflect
import sys


def main():
    dob = input("Date of Birth: ")
    validate_date(dob)


def validate_date(dob):
    convert = inflect.engine()
    pattern = r"\b(\d+)-(\d+)-(\d+)\b"
    matches = re.search(pattern, dob)
    if matches:
        try:
            entered_date = date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
            today = date.today()
            time_delta = int(str(today - entered_date).split(" ")[0])*24*60
            if time_delta >= 0:
                result = ((convert.number_to_words(time_delta)).capitalize()).split(" ")
                output = ''
                for word in result:
                    if not (word == "and"):
                        output += word + " "
                output += "minutes"
                print(output.strip())
                return True
            sys.exit("Invalid Date")
        except ValueError:
            sys.exit("Invalid Date")
    else:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()