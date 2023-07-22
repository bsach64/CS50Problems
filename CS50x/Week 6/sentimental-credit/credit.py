from cs50 import get_string
import re

def main():
    while True:
        input = get_string("Number: ")
        match = re.fullmatch('[0-9]+', input)
        if match:
            break

    input_digits = get_digits(input)
    length = len(input_digits)

    even_places_multiplied = []
    odd_places = []
    odd_places_sum = 0
    even_places_sum = 0
    even_places_digitized = []

    for i in range(length - 2, -1, -2):
        even_places_multiplied.append(2 * input_digits[i])

    for i in range(length - 1, -1, -2):
        odd_places.append(input_digits[i])
        odd_places_sum = odd_places_sum + input_digits[i]

    for i in range(0, len(even_places_multiplied)):
        tmp = str(even_places_multiplied[i])
        even_places_digitized.append(get_digits(tmp))

    for i in range(0, len(even_places_digitized)):
        for j in range(0, len(even_places_digitized[i])):
            even_places_sum = even_places_sum + even_places_digitized[i][j]

    sum = even_places_sum + odd_places_sum

    if sum % 10 == 0:
        if length == 15:
            if input_digits[0] == 3:
                if input_digits[1] == 4 or input_digits[1] == 7:
                    print("AMEX")
                else:
                    print("INVALID")
            else:
                print("INVALID")
        elif length == 16:
            if input_digits[0] == 5:
                if input_digits[1] == 1 or input_digits[1] == 2 or input_digits[1] == 3 or input_digits[1] == 4 or input_digits[1] == 5:
                    print("MASTERCARD")
                else:
                    print("INVALID")
            elif input_digits[0] == 4:
                print("VISA")
            else:
                print("INVALID")
        elif length == 13:
            if input_digits[0] == 4:
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")

def get_digits(n):
    str_number = str(n)
    length = len(str_number)
    digits = []
    for i in range(0, length):
        digits.append(int(str_number[i]))
    return digits

main()

'''
    American Express: 15 digit numbers (start with 34 or 37)
    MasterCard : 16 digit numbers (start with 51 - 55)
    Visa : 13 or 16 digit numbers (starts with a 4)
'''
