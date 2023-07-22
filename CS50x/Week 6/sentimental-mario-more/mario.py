def main():
    height = get_height()
    for i in range(height):
        for y in range(height - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print("  ", end="")
        for k in range(i + 1):
            print("#", end="")
        print()

# gets input from user and rejects invalid input

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                return n
        except ValueError:
            print("Not an integer")


main()