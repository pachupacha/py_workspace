while True:

    while True:
        user_number1 = int(input("Enter an integer: "))
        if (user_number1 != 0):
            break
        print("You cannot enter zero as a factor.")

    while True:
        user_number2 = int(input("Enter another integer: "))
        if (user_number2 != 0):
            break
        print("You cannot enter zero as a factor.")
    
    result = user_number1 / user_number2
    print(f"The result of {user_number1} divided by {user_number2} is {result}")
    continue_operation = input("Do you want to continue operating? Y/N: ").lower()
    if continue_operation == "n":
        break