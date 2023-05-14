import csv, re


pattern = r'\d{2}/\d{2}/2015.*'
primary_type = {}

with open('Crimes.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if re.match(pattern, row[2]):
            primary_type[row[5]] = primary_type.get(row[5], 0) + 1

primary_type = dict(sorted(primary_type.items(), key=lambda item: item[1], reverse=True))
print(primary_type)



