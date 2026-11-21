class Student:
    def __init__(self, student_id: str, name: str, program: str, grades: list[float]):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.grades = grades


def calculate_average(grades: list[float]) -> float:
    if not grades:
        raise ValueError("Grades list cannot be empty.")
    return sum(grades) / len(grades)


def evaluate_grade(average: float) -> str:
    if average < 0 or average > 100:
        raise ValueError("Average must be between 0 and 100.")
    if average >= 90:
        return "A (Excellent)"
    elif average >= 80:
        return "B (Very Good)"
    elif average >= 75:
        return "C (Passed)"
    else:
        return "F (Needs Improvement)"


def display_student_info(student: Student) -> None:
    avg = calculate_average(student.grades)
    standing = evaluate_grade(avg)
    print(f"ID       : {student.student_id}")
    print(f"Name     : {student.name}")
    print(f"Program  : {student.program}")
    print(f"Grades   : {student.grades}")
    print(f"Average  : {avg:.2f}")
    print(f"Standing : {standing}")