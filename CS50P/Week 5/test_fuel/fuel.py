

def main():
    fraction = input("Fraction: ").strip()
    while True:
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            ...


def convert(fraction):
    fraction = fraction.split('/')
    try:
        x = int(fraction[0])
        y = int(fraction[1])
        return round((x / y) * 100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
