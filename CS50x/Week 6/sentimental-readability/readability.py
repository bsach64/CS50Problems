def main():
    text = input("Text: ")
    letters = count_letter(text)
    words = count_word(text)
    sentences = count_sentences(text)
    l = (letters / words) * 100.0
    s = (sentences / words) * 100.0

    index = (0.0588 * l) - (0.296 * s) - 15.8
    if int(index) < 1:
        print("Before Grade 1")
    elif int(index) > 16:
        print("Grade 16+")
    else:
        if (index - int(index) > 0.5):
            print(f"Grade {int(index) + 1}")
        else:
            print(f"Grade {int(index)}")


def count_word(text):
    number = 1
    for letter in text:
        if letter == ' ':
            number += 1
    return number

def count_letter(text):
    number = 0
    for letter in text:
        if (letter >= 'a' and letter <= 'z'):
            number += 1
        elif (letter >= 'A' and letter <= 'Z'):
            number += 1
    return number

def count_sentences(text):
    number = 0
    for letter in text:
        if letter == '.' or letter == '!' or letter == '?':
            number += 1
    return number

main()
