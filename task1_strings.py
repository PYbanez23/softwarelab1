
full_name = input("Enter your full name: ")

uppercase_name = full_name.upper()
lowercase_name = full_name.lower()
char_count = len(full_name)

name_parts = full_name.split()
initials = "".join([part[0].upper() + "." for part in name_parts])

print("\n--- String Manipulation Results ---")
print("Uppercase:", uppercase_name)
print("Lowercase:", lowercase_name)
print("Total Characters (including spaces):", char_count)
print("Initials:", initials)