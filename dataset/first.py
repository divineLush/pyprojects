import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    first_col = [row[0] for row in reader]
    first_col.pop(0)
    print(first_col)
