while True:
    user_input = input("Enter your password: ").lower()
    if not user_input == "asereje":
        user_input2 = input("Incorrect password. You have one more chance. Enter your password: ").lower()
        if not user_input2 == "asereje":
            print("Access denied.")
            break
    else:
        print("Welcome user.")
    break