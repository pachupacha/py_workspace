while True:

    user_input = input("Please enter your name: ").lower().title()

    if not user_input.isalpha():
        print("You must enter a valid name.")
    elif user_input == "Alejandro":
        print("Welcome Alejandro.")
        break
    elif user_input == "Naomi":
        print("Welcome Naomi.")
        break
    elif user_input == "Sergio":
        print("Welcome Sergio.")
        break
    else:
        print("Welcome guest.")
        break