while True:
    user_input = input(
        "Enter the invested amount, the bot will tell you what procedure to follow: "
    )
    if not user_input.isdigit():
        print("You must enter a valid monetary value.")
        continue
    elif float(user_input) == 0:
        print("You cannot enter 0 as the monetary value.")
        continue
    elif float(user_input) < 100:
        print("You must buy.")
        continue
    elif float(user_input) >= 100 and float(user_input) <= 150:
        print("You must hold.")
        continue
    else:
        print("You must sell.")
        continue
