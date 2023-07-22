camel = input("camelCase: ")

for letter in camel:
    if letter.islower() == True:
        print(letter, end="")
    else:
        print("_" + letter.lower(), end="")
print()