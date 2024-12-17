user_number1 = int(input("Enter a number: ")) 
user_number2 = int(input("Enter a second number: "))
user_number3 = int(input("Enter a third number: "))

if user_number1 == user_number2 + user_number3:
    print(f"Your first number, {user_number1}, is the sum of your second number, {user_number2}, and your third number, {user_number3}.")
elif user_number2 == user_number1 + user_number3:
    print(f"Your second number, {user_number2}, is the sum of your first number, {user_number1}, and your third number, {user_number3}.")
elif user_number3 == user_number1 + user_number2:
    print(f"Your third number, {user_number3}, is the sum of your first number, {user_number1}, and your second number, {user_number2}.")
else:
    print("None of your numbers is the sum of the other two.")