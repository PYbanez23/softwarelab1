
class Person:
    def __init__(self, name, age, email):
       
        self.__name = name
        self.__age = age
        self.__email = email

  
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

  
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Email: {self.__email}")



class Student(Person):
    def __init__(self, name, age, email, student_id, course):
        super().__init__(name, age, email)
        self.__student_id = student_id
        self.__course = course


    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def display_info(self):
        print(f"[Student] ID: {self.__student_id} | Name: {self.get_name()} | Age: {self.get_age()} | Email: {self.get_email()} | Course: {self.__course}")


class Instructor(Person):
    def __init__(self, name, age, email, instructor_id, department):
        super().__init__(name, age, email)
        self.__instructor_id = instructor_id
        self.__department = department

    def display_info(self):
        print(f"[Instructor] ID: {self.__instructor_id} | Name: {self.get_name()} | Department: {self.__department}")



if __name__ == "__main__":
    print("--- Figure 12 & 13: Student Class & Encapsulation ---")
    student1 = Student("Christerpsalm Ybanez", 20, "christerpsalm@email.com", "20230001", "BSCpE")
    student1.display_info()
    
    
    student1.set_course("B.S. Computer Engineering")
    print("Updated Course:", student1.get_course())

    print("\n--- Figure 14: Inheritance Implementation ---")
    instructor1 = Instructor(1.4, 45, "engr.cruz@email.com", "INST-005", "Computer Engineering") 
    instructor1 = Instructor("Engr. Cruz", 45, "engr.cruz@email.com", "INST-005", "Computer Engineering")
    instructor1.display_info()

    print("\n--- Figure 15: Polymorphism Output ---")

    people = [student1, instructor1]
    for person in people:
        person.display_info()