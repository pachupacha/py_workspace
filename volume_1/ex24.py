while True:
    name_input = input("Enter your full name: ")
    if not name_input or name_input.isspace():
        print("You must enter a valid name.")
        continue
    elif not all(char.isalpha() or char.isspace() for char in name_input):
        print("You must enter a valid name.")
        continue
    space_count = name_input.count(" ")
    if space_count > 4:
        print(
            "Only a maximum of 5 words are allowed. Please enter a more simplified name."
        )
        continue

    gender_input = input("Enter your gender [M/F]: ").lower()
    if not gender_input.isalpha() or gender_input not in ["m", "f"]:
        print("You must enter a valid option.")
        continue
    if name_input:
        first_letter = name_input[0].upper()
    if first_letter in "EFGHIJKLM" and gender_input == "f":
        print(f"The female student {name_input.title()} will belong to group A")
        break
    elif first_letter in "ABCDNOPQRSTUVWXYZ" and gender_input == "f":
        print(f"The female student {name_input.title()} will belong to group B")
        break
    elif first_letter in "ABCDEFGHRSTUVWXYZ" and gender_input == "m":
        print(f"The male student {name_input.title()} will belong to group A")
        break
    else:
        if first_letter in "IJKLMNOPQ" and gender_input == "m":
            print(f"The male student {name_input.title()} will belong to group B")
            break
