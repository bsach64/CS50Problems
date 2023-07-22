def main():
    input_text = input("")
    print(convert(input_text))


def convert(string):
    if ":)" in string:
        string = string.replace(":)", "🙂")
    if ":(" in string:
        string = string.replace(":(", "🙁")
    return string

main()