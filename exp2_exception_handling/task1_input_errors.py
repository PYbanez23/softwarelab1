def get_grade():
    while True:
        try:
            grade = float(input("Enter student grade (0-100): "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            return grade
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Custom Error: Invalid input! Please enter a numeric grade.")
            else:
                print(f"Custom Error: {e}")


valid_grade = get_grade()
print(f"Recorded valid grade: {valid_grade}")