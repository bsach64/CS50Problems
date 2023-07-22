import sys
from tabulate import tabulate
import csv


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    extension = sys.argv[1][-4:]
    if extension != ".csv":
        sys.exit("Not a CSV file")
    else:
        line_count = 0
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")
        reader = csv.reader(file)
        print(tabulate((reader), tablefmt="grid", headers="firstrow"))
        file.close()

