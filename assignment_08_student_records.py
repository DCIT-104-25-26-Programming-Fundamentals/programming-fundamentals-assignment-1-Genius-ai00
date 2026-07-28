def display_menu():
    """Displays the student record system menu."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU   ")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Collects student details and scores, then adds them to the list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be at least 1.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for the number of scores.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input(f"Enter score {i}: "))
            
            if score.is_integer():
                score = int(score)
            scores.append(score)
        except ValueError:
            print("Invalid input. Defaulting score to 0.")
            scores.append(0)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students(students):
    """Displays all student records in a formatted table."""
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 50)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average':<8}")
    print("-" * 50)

    for s in students:
        scores_str = ", ".join(str(sc) for sc in s["scores"])
        avg = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0.0
        print(f"{s['name']:<15} {s['id']:<11} {scores_str:<14} {avg:.2f}")

    print("-" * 50)


def calculate_student_average(students):
    """Finds a student by ID and displays their average score."""
    if not students:
        print("No student records available.")
        return

    search_id = input("Enter student ID: ").strip()

    for s in students:
        if s["id"] == search_id:
            if s["scores"]:
                avg = sum(s["scores"]) / len(s["scores"])
                print(f"{s['name']}'s average score: {avg:.2f}")
            else:
                print(f"{s['name']} has no scores recorded.")
            return

    print(f"Error: Student ID '{search_id}' not found.")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()



