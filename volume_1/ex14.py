while True:

    user_input = input("Enter a password. It must contain at least one lowercase vowel and at least one special character (*, #): ")

    if not ("a" in user_input or "e" in user_input or "i" in user_input or "o" in user_input or "u" in user_input) or not ("*" in user_input or "#" in user_input):
        print("You must enter a secure password.")
    else:
        print("Your password is secure.")
        break