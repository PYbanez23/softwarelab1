from storage import load_records, save_records
import Utilities

DATA_FILE = "students_records.json"


def parse_grades(raw_grades: str) -> list[float]:
    parts = [p.strip() for p in raw_grades.split(",") if p.strip()]
    if not parts:
        raise ValueError("Please enter at least one grade.")
    grades = [float(p) for p in parts]
    for g in grades:
        if g < 0 or g > 100:
            raise ValueError(f"Grade {g} is out of range (0-100).")
    return grades


def add_student(records: list[dict]) -> None:
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    program = input("Enter Program (e.g., BSCpE): ").strip()
    if not student_id or not name or not program:
        raise ValueError("ID, Name, and Program cannot be empty.")

    raw_grades = input("Enter grades separated by commas (e.g., 90, 85, 88): ")
    grades = parse_grades(raw_grades)

    records.append({
        "id": student_id,
        "name": name,
        "program": program,
        "grades": grades,
    })
    save_records(records, DATA_FILE)
    print("Student added successfully.")


def view_students(records: list[dict]) -> None:
    if not records:
        print("No student records found.")
        return
    print("\n=== Student Records ===")
    for idx, rec in enumerate(records, start=1):
        print(f"\n--- Record #{idx} ---")
        student = Utilities.Student(rec["id"], rec["name"], rec["program"], rec["grades"])
        Utilities.display_student_info(student)


def main() -> None:
    records = load_records(DATA_FILE)
    print(f"Loaded {len(records)} existing record(s) from '{DATA_FILE}'.")

    while True:
        print("\n1. Add Student")
        print("2. View All Students (with Average & Standing)")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        try:
            if choice == "1":
                add_student(records)
            elif choice == "2":
                view_students(records)
            elif choice == "3":
                save_records(records, DATA_FILE)
                print("Exiting program.")
                break
            else:
                raise ValueError("Invalid menu choice. Enter 1, 2, or 3.")
        except ValueError as e:
            print(f"Input Error: {e}")


if __name__ == "__main__":
    main()