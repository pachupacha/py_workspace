import time
import os

students_full_names = []
homework_grades = []
exam_grades = []
project_grades = []
students_data = []


def clear_screen():
    os.system("cls")


def calculate_average(homework, exam, project):
    return (homework + exam + project) / 3


while True:
    while True:
        name = input("Enter your first name: ").title()
        if not name.isalpha():
            clear_screen()
            print("Please enter a valid first name (only alphabetic characters).")
        else:
            break

    while True:
        surname = input("Enter your surname: ").title()
        if not surname.isalpha():
            clear_screen()
            print("Please enter a valid surname (only alphabetic characters).")
        else:
            break

    clear_screen()
    full_name = f"{name} {surname}"
    students_full_names.append(full_name)

    while True:
        homework_grade = float(input("Enter the Homework grade: "))
        if homework_grade < 0 or homework_grade > 10.0:
            clear_screen()
            print("Please enter a valid grade.")
        else:
            clear_screen()
            homework_grades.append(homework_grade)
            break

    while True:
        exam_grade = float(input("Enter the exam grade: "))
        if exam_grade < 0 or exam_grade > 10.0:
            clear_screen()
            print("Please enter a valid grade.")
        else:
            clear_screen()
            exam_grades.append(exam_grade)
            break

    while True:
        project_grade = float(input("Enter the Project grade: "))
        if project_grade < 0 or project_grade > 10.0:
            clear_screen()
            print("Please enter a valid grade.")
        else:
            clear_screen()
            project_grades.append(project_grade)
            break

    student_complete_profile = [
        students_full_names[-1],
        homework_grades[-1],
        exam_grades[-1],
        project_grades[-1],
    ]
    students_data.append(student_complete_profile)

    while True:
        continue_input = input(
            "Do you want to add another student?\nInput '1' to Continue.\nInput '2' to Get Final Dashboard.\n"
        )
        if continue_input == "1":
            clear_screen()
            break
        elif continue_input == "2":
            clear_screen()
            print("Loading Students Dashboard...")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("Please, insert a valid option. Select '1' or '2'. ")

    if continue_input == "2":
        break

clear_screen()
print("Final Dashboard:")
for student in students_data:
    name = student[0]
    homework = student[1]
    exam = student[2]
    project = student[3]

    average = calculate_average(homework, exam, project)

    if average < 4:
        promotion_status = "DOES NOT PROMOTE"
    else:
        promotion_status = "PROMOTES"

    print(f"\nName: {name}")
    print(f"Homework: {homework}")
    print(f"Exam: {exam}")
    print(f"Project: {project}")
    print(f"Average: {average:.2f}")
    print(f"Promotion Status: {promotion_status}")
    print("\n" + "-" * 30 + "\n")
