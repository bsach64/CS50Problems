vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

text = input("Input: ")

print("Output: ", end="")
for letter in text:
    if letter not in vowels:
        print(letter, end="")

print()