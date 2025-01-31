import random
import os
import time


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def censor_word(word, symbols):
    """Replaces an offensive word with random symbols."""
    return "".join(random.choice(symbols) for _ in range(len(word)))


def handle_message(
    username,
    text,
    symbols,
    offensive_words,
    warnings,
    penalty_durations,
    current_penalty_index,
):
    """Processes the user's text, checks for offensive content, and handles penalties."""
    modified_text = []
    contains_offensive = False

    for word in text.split():
        if word.lower() in offensive_words:
            contains_offensive = True
            modified_text.append(censor_word(word, symbols))
        else:
            modified_text.append(word)

    result = " ".join(modified_text)

    if contains_offensive:
        warnings += 1
        if warnings >= 5:
            if current_penalty_index < len(penalty_durations):
                duration = penalty_durations[current_penalty_index]
                current_penalty_index += 1
            else:
                duration = 86400
            warnings = 0
            return (
                warnings,
                current_penalty_index,
                f"[{username}]: {result}\nDue to disruptive behavior, you cannot send messages for {duration//60:02}:{duration%60:02}. "
                f"If this continues, penalties will increase.",
                duration,
            )
        else:
            return (
                warnings,
                current_penalty_index,
                f"Warning {warnings}/5: Inappropriate language detected.\n[{username}]: {result}",
                0,
            )
    else:
        return warnings, current_penalty_index, f"[{username}]: {result}", 0


symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~"]
offensive_words = ["word1", "word2", "word3", "word4", "word5", "word6"]
warnings = 0
penalty_durations = [5, 15, 30, 45]
current_penalty_index = 0
chat_history = []
penalized = False
penalty_end_time = 0

clear_screen()
username = input("What is your nickname?: ").strip()
clear_screen()
print(f"Hello {username}, welcome to the game!")

while True:

    if penalized:
        current_time = time.time()
        remaining_time = int(penalty_end_time - current_time)
        if remaining_time <= 0:
            penalized = False
            continue
        else:

            print(
                f"Due to disruptive behavior, you cannot send messages for {remaining_time//60:02}:{remaining_time%60:02}. "
                f"If this continues, penalties will increase."
            )
            input()
            clear_screen()
            print("=== Chat ===")
            for msg in chat_history:
                print(msg)
            continue

    user_input = input(f"[{username}]: ").strip()

    if not user_input:
        clear_screen()
        print("=== Chat ===")
        for msg in chat_history:
            print(msg)
        continue

    warnings, current_penalty_index, message, penalty_duration = handle_message(
        username,
        user_input,
        symbols,
        offensive_words,
        warnings,
        penalty_durations,
        current_penalty_index,
    )

    if penalty_duration > 0:
        penalized = True
        penalty_end_time = time.time() + penalty_duration
        chat_history.append(message)
    else:
        chat_history.append(message)

    clear_screen()
    print("=== Chat ===")
    for msg in chat_history:
        print(msg)