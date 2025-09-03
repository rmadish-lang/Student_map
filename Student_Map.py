def get_student_name(student_map: dict[int, str], student_id: int) -> str:
    """Return the student name for the given ID.
    If the ID is not found, return "Unknown".
    """
    return student_map.get(student_id, "Unknown")


def add_student(student_map: dict[int, str], student_id: int, name: str) -> None:
    """Add a new student to the map (id → name).
    If the id already exists, replace the old name.
    """
    student_map[student_id] = name


def remove_student(student_map: dict[int, str], student_id: int) -> None:
    """Remove a student from the map by id.
    If the id is not found, do nothing.
    """
    student_map.pop(student_id, None)


def print_all_students(student_map: dict[int, str]) -> None:
    """Print all students in the format:
    ID: <id>, Name: <name>
    One per line.
    """
    for student_id, name in student_map.items():
        print(f"ID: {student_id}, Name: {name}")


if __name__ == "__main__":
    # Initial dictionary of students
    students = {
        101: "Alice",
        102: "Bob",
        103: "Charlie"
    }
    print("Original student list:")
    print_all_students(students)
    print()
    print("Look up ID 102:", get_student_name(students, 102))
    print("Look up ID 999:", get_student_name(students, 999))
    print()
    print("Adding new student 104: Diana")
    add_student(students, 104, "Diana")
    print_all_students(students)
    print()
    print("Removing student 101")
    remove_student(students, 101)
    print_all_students(students)
