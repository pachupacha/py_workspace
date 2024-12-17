user_input = input("Enter a 4-digit number: ")
per_line_number = (
    user_input[0] + "\n" + user_input[1] + "\n" + user_input[2] + "\n" + user_input[3]
)
inverted_number = user_input[3] + user_input[2] + user_input[1] + user_input[0]
print(per_line_number)
print("\n")
print(inverted_number)

