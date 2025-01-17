import os

while True:
    os.system("cls")
    print("Palindrome Checker")

    text = input("Enter a word or phrase: ").strip()
    if not text:
        print("Error: No valid input provided. Try again.")
        input("Press Enter to continue...")
        continue

    valid_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    processed_text = "".join(c.lower() for c in text if c.lower() in valid_characters)

    # Verificar si es un palíndromo
    if processed_text == processed_text[::-1]:
        print("\nYes, it's a palindrome!")
    else:
        print("\nNo, it's not a palindrome.")

    retry = input("\nDo you want to check another word or phrase? (Y/N): ").strip().lower()
    if retry != "y":
        break
