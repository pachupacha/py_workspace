import random
import os


def clear_screen():
    os.system("cls")



while True:
    text = input("input a text: ").lower().split()
    symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~"]
    offensive_words = ["placeholder_1", "placeholder_2", "placeholder_3", "placeholder_4", "placeholder_5", "placeholder_6"]
    modified_text = []
    for word in text:
        if word in offensive_words:
            modified_text.append("".join(random.choice(symbols) for _ in range(len(word))))
        else:
            modified_text.append(word)
    result = "".join(modified_text)
    print(result)