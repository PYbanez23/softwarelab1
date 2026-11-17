# ==========================================
# POSTLAB: Student Management System
# ==========================================

# --- OBJECT-ORIENTED PROGRAMMING (OOP) ---

class Person:
    def __init__(self, name, age, email):
        # Encapsulation: Private attributes
        self.__name = name
        self.__age = age
        self.__email = email

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"Name: {self.__name} | Age: {self.__age} | Email: {self.__email}")


# Inheritance: Student inherits from Person
class Student(Person):
    def __init__(self, student_id, name, age, email, course, grades=None):
        super().__init__(name, age, email)
        self.__student_id = student_id
        self.__course = course
        # Using a List for grades
        self.__grades = grades if grades else []

    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_grades(self):
        return self.__grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def compute_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    # Polymorphism: Overriding display_info method
    def display_info(self):
        avg = self.compute_average()
        print(f"[Student Record] ID: {self.__student_id} | Name: {self.get_name()} | Course: {self.__course} | Grades: {self.__grades} | Average: {avg:.2f}")


# Inheritance: Instructor inherits from Person
class Instructor(Person):
    def __init__(self, instructor_id, name, age, email, department):
        super().__init__(name, age, email)
        self.__instructor_id = instructor_id
        self.__department = department

    def get_instructor_id(self):
        return self.__instructor_id

    # Polymorphism: Overriding display_info method
    def display_info(self):
        print(f"[Instructor Record] ID: {self.__instructor_id} | Name: {self.get_name()} | Department: {self.__department}")


# --- SYSTEM CONTROLLER & DATA STRUCTURES ---

class StudentManagementSystem:
    def __init__(self):
        # Dictionary for student records (Key: Student ID, Value: Student Object)
        self.students = {}
        
        # Tuple for fixed course information (Course Code, Description, Units)
        self.course_info = ("CPE101", "Computer Engineering Fundamentals", 3)

    def add_student(self, student_id, name, age, email, course, grades):
        if student_id in self.students:
            print(f"Error: Student ID {student_id} already exists.")
        else:
            new_student = Student(student_id, name, age, email, course, grades)
            self.students[student_id] = new_student
            print(f"Success: Student {name} added successfully.")

    def update_student(self, student_id, new_course):
        if student_id in self.students:
            self.students[student_id].set_course(new_course)
            print(f"Success: Student {student_id} course updated to {new_course}.")
        else:
            print(f"Error: Student ID {student_id} not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Success: Student {student_id} deleted.")
        else:
            print(f"Error: Student ID {student_id} not found.")

    def search_student(self, student_id):
        if student_id in self.students:
            print("\n--- Search Result ---")
            self.students[student_id].display_info()
        else:
            print(f"Error: Student ID {student_id} not found.")

    def display_all_records(self):
        print("\n--- All Student Records ---")
        if not self.students:
            print("No student records available.")
        for student in self.students.values():
            student.display_info()

    def display_course_info(self):
        print("\n--- Fixed Course Information (Tuple) ---")
        code, description, units = self.course_info
        print(f"Course Code: {code}")
        print(f"Description: {description}")
        print(f"Units: {units}")


# --- EXECUTION / TESTING ---
if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Display Course Info (Tuple)
    sms.display_course_info()

    # Add Students (Dictionaries & Lists)
    sms.add_student("2023-001", "Christerpsalm Ybanez", 20, "christerpsalm@email.com", "Computer Engineering", [90.0, 85.5, 92.0])
    sms.add_student("2023-002", "Juan Dela Cruz", 21, "juan@email.com", "Information Technology", [88.0, 79.5, 84.0])

    # Display All Records
    sms.display_all_records()

    # Search Student
    sms.search_student("2023-001")

    # Update Student Record
    sms.update_student("2023-001", "BS Computer Engineering (Advanced)")

    # Delete Student Record
    sms.delete_student("2023-002")

    # Final Display
    sms.display_all_records()
    
    # Test Instructor (Inheritance & Polymorphism)
    print("\n--- Instructor Information ---")
    instructor = Instructor("INST-005", "Engr. Cruz", 42, "cruz@email.com", "ECE Department")
    instructor.display_info()