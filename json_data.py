import json

data = {
  "name": "John",
  "age": 30,
  "city": "New York",
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file) 

print("Data written to data.json")

with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Data read from data.json:", loaded_data)
