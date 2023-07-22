def main():
    word = input("Input: ")
    print("Output:" + shorten(word))


def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, '')
    return word


if __name__ == "__main__":
    main()