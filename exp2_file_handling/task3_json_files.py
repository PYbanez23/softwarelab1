import json

json_file = "students.json"
students = [
    {"id": "2024001", "name": "Ana Santos", "course": "BSCpE", "year": 3},
    {"id": "2024002", "name": "Marco Reyes", "course": "BSCpE", "year": 3},
]

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("=== JSON Contents ===")
with open(json_file, "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=4))

loaded_data.append({"id": "2024003", "name": "Lianne Cruz", "course": "BSCpE", "year": 3})
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(loaded_data, file, indent=4)

print("\n=== Updated JSON Contents ===")
with open(json_file, "r", encoding="utf-8") as file:
    updated_data = json.load(file)
    print(json.dumps(updated_data, indent=4))