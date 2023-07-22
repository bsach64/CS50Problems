x, y, z = input("Expression: ").split(" ")

if y == '+':
    print(round((float(x) + float(z)), 2))
elif y == '/':
    print(round((float(x) / float(z)), 2))
elif y == '*':
    print(round((float(x) * float(z)), 2))
elif y == '-':
    print(round((float(x) - float(z)), 2))