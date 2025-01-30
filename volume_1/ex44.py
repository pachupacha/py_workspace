LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

def calculate_score(word):
    total = 0
    for letter in word.upper():
        if letter in LETTER_VALUES:
            total += LETTER_VALUES[letter]
        else:
            print(f"Ignored invalid character: {letter}")
    return total

while True:
    user_input = input("\nEnter a word (or 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        break
        
    if not user_input.isalpha():
        print("Only letters are allowed!")
        continue
        
    score = calculate_score(user_input)
    print(f"Word '{user_input.upper()}' scores {score} Scrabble points")

print("\nGoodbye!")