while True:
    user_input = input(
        "Enter a letter, the bot will tell you if it is uppercase or lowercase: "
    )
    if len(user_input) != 1:
        print("ERROR: You must enter only one character.")
        continue
    elif not user_input.isalpha():
        print("ERROR: You must enter only a letter.")
        continue

    if user_input.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")
    break
