import json
import csv

with open("json/users.json") as f:
    result = json.load(f)
#print(result)

result = []
with open('csv/books.csv') as f:
    reader = csv.reader(f)
print(reader)
header = next(reader)
for row in reader:
    item = dict(zip(header, row))
    result.append(item)

print(result)
