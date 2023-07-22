import random
import sys

def main():
    level = get_level()
    score = 0
    for i in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        for j in range(0, 3):
            print(x ,"+", y, end=" = ")
            try:
                answer = int(input())
            except ValueError:
                ...
            if answer == (x + y):
                score += 1
                break
            else:
                print("EEE")
            if answer != (x + y) and j == 2:
                print(x, "+", y, "=", (x + y))
        if i == 9:
            print("Score: " ,score)
            sys.exit(0)

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x not in [1, 2, 3]:
                raise ValueError
            else:
                return x

        except ValueError:
            ...


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()