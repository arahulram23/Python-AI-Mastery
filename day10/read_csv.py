import csv

with open ("expenses.csv","r")as file:

    reader = csv.DictReader(file)
    for row in reader:
        print(row)