import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        source_file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    dest_file = open(sys.argv[2], "w", newline='')
    reader = csv.DictReader(source_file)
    fieldnames = ["first","last","house"]
    writer = csv.DictWriter(dest_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        last,first = row['name'].split(',')
        writer.writerow({'first': first.strip(), 'last': last.strip(), 'house': row['house']})