import os


def clear_screen():
    os.system("cls")


while True:
    odd_numbers = []
    even_numbers = []
    user_input = input(
        "Please, input up to 10 numbers separated by spaces (maximum 2 digits per number): "
    )

    if not user_input.strip():
        clear_screen()
        print("You must input at least one number.")
        continue

    numbers = user_input.split()

    if len(numbers) > 10:
        clear_screen()
        print("You can only input up to 10 numbers. Try again.")
        continue

    valid_numbers = []
    for num in numbers:
        if num.isdigit() and 1 <= len(num) <= 2:
            valid_numbers.append(int(num))
        else:
            clear_screen()
            print(
                f"Invalid input: '{num}' is not a valid number (must be up to 2 digits). Try again."
            )
            break
    else:

        for num in valid_numbers:
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

        print(f"Even numbers: {even_numbers}")
        print(f"Odd numbers: {odd_numbers}")
        print(f"Total even numbers: {len(even_numbers)}")
        print(f"Total odd numbers: {len(odd_numbers)}")

    reusage = input("Do you want to use the system again? (Y/N): ").lower()
    if reusage == "y":
        clear_screen()
        continue
    else:
        clear_screen()
        print("Thank you for using the system. Goodbye!")
        break
