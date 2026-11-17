
student = {
    "StudentID": "20230001",
    "Name": "Juan Dela Cruz",
    "Course": "BSCpE"
}

print("Original Dictionary:", student)


student["YearLevel"] = "3rd Year"
print("\nAfter Adding 'YearLevel':", student)

student["Course"] = "BS Computer Engineering"
print("After Updating 'Course':", student)


print("Retrieved Student Name:", student["Name"])
print("Retrieved Student ID:", student.get("StudentID"))

del student["YearLevel"]
print("After Deleting 'YearLevel':", student)