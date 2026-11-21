import csv

csv_file = "students.csv"
rows = [
    ["ID", "Name", "Course", "Year"],
    ["2024001", "Ana Santos", "BSCpE", "3"],
    ["2024002", "Marco Reyes", "BSCpE", "3"],
]

# 1. Write rows to students.csv
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# 2. Read and display CSV contents
print("=== CSV Contents ===")
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 3. Append a new student row
with open(csv_file, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["2024003", "Lianne Cruz", "BSCpE", "3"])

# 4. Read and display updated CSV contents
print("\n=== Updated CSV Contents ===")
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)