import os

def clear_screen():
    os.system('cls')

while True:
    clear_screen()
    sentence = input("Enter a sentence or phrase: ").strip()

    if not sentence:
        print("Error: No valid words entered. Please try again.")
        input("Press Enter to continue...")
        continue

    # Convert to lowercase and remove punctuation
    sentence = sentence.lower()
    for char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
        sentence = sentence.replace(char, "")

    # Split into words and get unique sorted words
    words = sentence.split()
    unique_words = sorted(set(words))

    if unique_words:
        print(f"\nNumber of unique words: {len(unique_words)}")
        print("Unique words (sorted alphabetically):")
        print(", ".join(unique_words))
    else:
        print("Error: No valid words entered. Please try again.")

    repeat = input("\nDo you want to enter another sentence? (Y/N): ").strip().lower()
    if repeat != 'y':
        break

