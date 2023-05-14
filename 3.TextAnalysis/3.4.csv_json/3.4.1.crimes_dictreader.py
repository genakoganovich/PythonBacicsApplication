import csv
from datetime import datetime

primary_type = {}

with open('Crimes.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if datetime.strptime(row['Date'], '%m/%d/%Y %I:%M:%S %p').year == 2015:
            primary_type[row['Primary Type']] = primary_type.get(row['Primary Type'], 0) + 1

primary_type = dict(sorted(primary_type.items(), key=lambda item: item[1], reverse=True))
print(primary_type)
