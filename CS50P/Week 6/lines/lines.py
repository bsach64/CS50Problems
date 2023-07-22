import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    extension = sys.argv[1][-3:]
    if extension != ".py":
        sys.exit("Not a Python file")
    else:
        line_count = 0
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")
        all_lines = file.readlines()
        for line in all_lines:
            if line.isspace() == True:
                ...
            elif "#" in line.lstrip()[0]:
                ...
            else:
                line_count += 1
        file.close()
        print(line_count)