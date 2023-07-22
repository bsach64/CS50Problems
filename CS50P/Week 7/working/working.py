import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d+)(:)?(\d+)?\s(A|P)M\sto\s(\d+)(:)?(\d+)?\s(A|P)M"
    matches = re.search(pattern, s)
    if matches:
        final_output = ""
        hour_one = hour_calculator(matches.group(1), matches.group(4))
        final_output = final_output + hour_one
        hour_two = hour_calculator(matches.group(5), matches.group(8))
        if matches.group(3) != None:
            minute_one = minute_calculator(matches.group(3))
        else:
            minute_one = "00"
        final_output = final_output + ":" + minute_one + " to " + hour_two
        if matches.group(7) != None:
            minute_two = minute_calculator(matches.group(7))
        else:
            minute_two = "00"
        final_output = final_output + ":" + minute_two
        return final_output
    else:
        raise ValueError

# Group 1 (Hour_One)
# Group 4 (M_One)
# Group 5 (Hour_Two)
# Group 8 (M_Two)
# Group 3 (Minute_One)
# Group 7 (Minute_Two)

def hour_calculator(hour, letter):
    if int(hour) >= 1 and int(hour) <= 12:
        if letter == "A":
            if int(hour) < 10:
                return ("0" + hour)
            if int(hour) == 12:
                return "00"
            return hour
        elif letter == "P":
            if int(hour) == 12:
                return hour
            return str(int(hour) + 12)
    else:
        raise ValueError

def minute_calculator(minute):
    if int(minute) >= 0 and int(minute) < 60:
        return minute
    else:
        raise ValueError

if __name__ == "__main__":
    main()
