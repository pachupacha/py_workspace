user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))
user_number3 = int(input("Enter the third number: "))
user_number4 = int(input("Enter the fourth number: "))

if user_number1 >= user_number2:
    if user_number1 >= user_number3:
        if user_number1 >= user_number4:
            largest = user_number1
        else:
            largest = user_number4
    elif user_number3 >= user_number4:
        largest = user_number3
    else:
        largest = user_number4
else:
    if user_number2 >= user_number3:
        if user_number2 >= user_number4:
            largest = user_number2
        else:
            largest = user_number4
    elif user_number3 >= user_number4:
        largest = user_number3
    else:
        largest = user_number4

print(f"The largest number is {largest}")