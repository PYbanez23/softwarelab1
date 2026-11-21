import Utilities

student1 = Utilities.Student("2024001", "Ana Santos", "BSCpE", [92.0, 88.5, 95.0])
student2 = Utilities.Student("2024002", "Marco Reyes", "BSCpE", [78.0, 81.0, 76.5])

print("=== Student 1 Summary ===")
Utilities.display_student_info(student1)

print("\n=== Student 2 Summary ===")
Utilities.display_student_info(student2)