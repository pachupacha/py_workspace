import os

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
result = ""


def clear_screen():
    os.system("cls")


while True:
    user_input = input(
        "Please, input your phrase. It will be changed to ROT13: "
    ).lower()

    if not all(char.isalpha() or char.isspace() for char in user_input):
        clear_screen()
        print("Numbers and Symbols not Allowed. Try Again.")
        continue
    else:
        result = ""
        for c in user_input:
            if c in alphabet:
                user_letter_index = alphabet.index(c)
                new_index = (user_letter_index + 13) % 26
                result += alphabet[new_index]
            else:
                result += c

        print(f"Your Text in ROT13 is: {result}")