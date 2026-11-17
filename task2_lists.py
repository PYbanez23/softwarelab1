
grades = []

for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades.append(grade)

average_grade = sum(grades) / len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)
sorted_grades = sorted(grades)

print("\n--- List Operations Results ---")
print("Grades List:", grades)
print(f"Average Grade: {average_grade:.2f}")
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)
print("Sorted Grades (Ascending):", sorted_grades)