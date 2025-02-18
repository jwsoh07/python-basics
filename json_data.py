import json
import csv

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
    {"name": "Tom", "age": 35, "city": "Chicago"}
]

with open("data.json", "w") as json_file:
    json.dump(data, json_file) 

print("Data written to data.json")

with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Data read from data.json:", loaded_data)

# Write data to a CSV file
with open("people.csv", "w", newline="") as csvfile:
  fieldnames = ["name", "age", "city"] # Column names
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(data)

# Read the CSV file and print each row
with open("people.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)