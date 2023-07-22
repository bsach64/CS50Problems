
while True:
    fraction = input("Fraction: ").strip()
    fraction = fraction.split('/')
    try:
        x = int(fraction[0])
        y = int(fraction[1])
        z = (x / y)
        if x <= y:
            if z >= 0 and z <= 0.01:
                print("E")
            elif z >= 0.99 and z <= 1:
                print("F")
            else:
                print(str(round(z * 100)) + "%")
            break
    except (ValueError, ZeroDivisionError):
        fraction = input("Fraction: ").strip()