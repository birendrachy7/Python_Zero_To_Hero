# json:
import json


data = {
    "name": "BoB",
    "age": 30,
    "city": "Dhnagadhi"
}

#writing the json
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data,file,
        indent=4,          # 4-space indentation
        sort_keys=True,      #Sort key alphabetic key
        ensure_ascii=False # preserve Unicode characters
    )
#reading the json
with open("data.json", "r") as file:
    data = json.load(file)

print(data)