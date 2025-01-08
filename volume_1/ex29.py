number_list = []
while True:
    user_range = input('How many numbers you do want to sort?: ')
    
    if not user_range.isdigit():
        print('Please input a valid number.')
    elif int(user_range) > 50:
        print('The maximum numbers for sorting is 50.\nPlease input fewer numbers to sort.')
    else:
        for i in range(int(user_range)):
            num_input = input(f"Input number {i + 1}: ")
            while not num_input.isdigit():  # Verifica si el número ingresado es válido
                print("Please input a valid integer number.")
                num_input = input(f"Input number {i + 1}: ")
            number_list.append(int(num_input))

        number_list.sort()
        max_number = max(number_list)
        print(number_list)
        print(f"The highest number is {max_number}.")
        break