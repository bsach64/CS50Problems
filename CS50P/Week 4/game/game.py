import random

def main():
    level = get_int("Level: ")
    answer = random.randrange(1, level + 1)
    while True:
        guess = get_int("Guess: ")

        if answer == guess:
            print("Just Right!")
            break
        elif answer > guess:
            print("Too Small!")

        elif answer < guess:
            print("Too Large!")

def get_int(s):
    while True:
        try:
            integer = int(input(s))
            if integer > 0:
                return integer
        except ValueError:
            ...

if __name__ == "__main__":
    main()