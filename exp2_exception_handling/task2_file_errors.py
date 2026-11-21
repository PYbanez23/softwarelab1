filename = input("Enter the filename to open (e.g., missing_grades.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("\n=== File Contents ===")
        print(content)
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' could not be found. Please check the file name and try again.")
except PermissionError:
    print(f"Sorry, you don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred while opening '{filename}': {e}")