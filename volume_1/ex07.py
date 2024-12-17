card_number = input("Enter the 16 digits of your credit card without spaces: ")

length = len(card_number)
asterisks = "*" * (length - 4)
last_digits = card_number[-4:]
result = asterisks + last_digits
print(result)
