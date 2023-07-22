import csv

with open("databases/small.csv", "r") as file:
    reader = csv.DictReader(file)


with open("sequences/1.txt", "r") as file:
    reader = file.readlines()
    dna = reader[0].replace('\n','')


