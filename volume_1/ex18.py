while True:
    name = input("Enter your name: ").title()
    if not name.isalpha():
        print("Please enter a valid name.")
    else: 
        break

while True:
    while True:
        age = input("Enter your age: ")
        if not age.isdigit() or '.' in age or int(age) > 100:
            print("Please enter a valid age.")
        else:
            break
    if int(age) < 17 or int(age) > 21:
        print("You don't meet the age requirements for the scholarship.")
        break
    break

if int(age) >= 17 and int(age) <= 21:
    while True:
        while True:
            first_term_grade = float(input("Enter the final grade of the first semester: "))
            if first_term_grade < 0 or first_term_grade > 10.0:
                print("Please enter a valid grade")
            else:
                break

        while True:
            second_term_grade = float(input("Enter the final grade of the second semester: "))
            if second_term_grade < 0 or second_term_grade > 10.0:
                print("Please enter a valid grade")
            else:
                break

        while True:
            third_term_grade = float(input("Enter the final grade of the third semester: "))
            if third_term_grade < 0 or third_term_grade > 10.0:
                print("Please enter a valid grade")
            else:
                break

        final_grade = (first_term_grade + second_term_grade + third_term_grade) / 3

        if final_grade <= 8:
            print(f"Final average grade: {final_grade}")
            print("You don't meet the academic requirements for the scholarship.")
        else:
            print(f"Final average grade: {final_grade}")
            print(f"Congratulations {name}, you meet all the requirements for the scholarship.")
        break