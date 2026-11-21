file_name = "students.txt"

# 1. Create students.txt and write initial student information
with open(file_name, "w", encoding="utf-8") as file:
    file.write("ID: 2024001 | Name: Ana Santos | Course: BSCpE\n")
    file.write("ID: 2024002 | Name: Marco Reyes | Course: BSCpE\n")

# 2. Read and display the file contents
print("=== Initial File Contents ===")
with open(file_name, "r", encoding="utf-8") as file:
    print(file.read(), end="")

# 3. Append additional student records
with open(file_name, "a", encoding="utf-8") as file:
    file.write("ID: 2024003 | Name: Lianne Cruz | Course: BSCpE\n")
    file.write("ID: 2024004 | Name: Noah Lim | Course: BSCpE\n")

# 4. Read and display updated file contents
print("\n=== Updated File Contents After Append ===")
with open(file_name, "r", encoding="utf-8") as file:
    print(file.read(), end="")