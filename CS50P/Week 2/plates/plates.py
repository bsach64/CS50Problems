def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s.isalnum():
            if s[0:2].isalpha():
                letter = True
                number = False
                for i in range(2, len(s)):
                    if s[i].isalpha():
                        letter = True
                        if number == True:
                            return False
                    else:
                        if number == False:
                            if s[i] == '0':
                                return False
                        letter = False
                        number = True
                if letter == True and number == False:
                    return True
                elif letter == False and number == True:
                    return True

    return False

main()