import os
import time


def clear_screen():
    os.system('cls')


def show_fruits(fruits):
    clear_screen()
    if fruits:
        print("\nAvailable fruits:")
        for i, fruit in enumerate(fruits, start=1):
            print(f"{i}. {fruit}")
    else:
        print("\nNo fruits available in the list.")
        time.sleep(2)
        clear_screen()


def add_fruit(fruits):
    while True:
        clear_screen()
        new_fruit = input("Enter the name of the fruit you want to add (R to go back): ").strip()
        if new_fruit.upper() == "R":
            print("\nGoing back to the main menu...")
            time.sleep(2)
            clear_screen()
            break
        elif not new_fruit.isalpha():
            print("\nError: Only letters are allowed. Please try again.")
            time.sleep(2)
            clear_screen()
        elif new_fruit in fruits:
            print(f"\n'{new_fruit}' already exists in the list. No duplicates allowed.")
            time.sleep(2)
            clear_screen()
        else:
            fruits.append(new_fruit)
            print(f"\n'{new_fruit}' has been added to the list.")
            time.sleep(2)
            clear_screen()
            break


def remove_fruit(fruits):
    while True:
        clear_screen()
        if not fruits:
            print("\nThe fruit list is empty. Nothing to remove.")
            time.sleep(2)
            clear_screen()
            break

        show_fruits(fruits)
        fruit_to_remove = input("Enter the name of the fruit you want to remove (R to go back): ").strip()
        
        if fruit_to_remove.upper() == "R":
            print("\nGoing back to the main menu...")
            time.sleep(2)
            clear_screen()
            break
        elif fruit_to_remove in fruits:
            fruits.remove(fruit_to_remove)
            print(f"\n'{fruit_to_remove}' has been removed from the list.")
            time.sleep(2)
            clear_screen()
            if not fruits:
                print("\nAll fruits have been removed. The list is empty.")
                time.sleep(2)
                clear_screen()
            break
        else:
            print(f"\n'{fruit_to_remove}' is not in the list.")
            time.sleep(2)
            clear_screen()

def search_long_fruits(fruits):
    while True:
        clear_screen()
        if not fruits:
            print("\nThe fruit list is empty.")
            time.sleep(2)
            clear_screen()
            break

        length = input("Enter the minimum number of characters (R to go back): ").strip()
        if length.upper() == "R":
            print("\nGoing back to the main menu...")
            time.sleep(2)
            clear_screen()
            break
        elif not length.isdigit():
            print("\nError: You must enter a valid number. Please try again.")
            time.sleep(2)
            clear_screen()
        else:
            length = int(length)
            print(f"\nFruits with more than {length} characters:")
            for fruit in fruits:
                if len(fruit) > length:
                    print(fruit)
            break

# Main program
fruits = ["apple", "banana", "cherry", "pear", "fig", "raspberry", "strawberry"]

while True:
    
    print("\n--- Grocery Store Menu ---")
    print("1. Show available fruits")
    print("2. Add a fruit")
    print("3. Remove a fruit")
    print("4. Search for long-named fruits")
    print("5. Exit")
    print("R. Go back to the main menu")

    option = input("Select an option: ").strip().upper()

    if option == "1":
        show_fruits(fruits)
    elif option == "2":
        add_fruit(fruits)
    elif option == "3":
        remove_fruit(fruits)
    elif option == "4":
        search_long_fruits(fruits)
    elif option == "5":
        clear_screen()
        print("\nThank you for using the grocery store management system. Goodbye!")
        time.sleep(2)
        break
    elif option == "R":
        clear_screen()
        print("\nGoing back to the main menu...")
        time.sleep(2)
        clear_screen()
    else:
        clear_screen()
        print("\nInvalid option. Please try again.")
        time.sleep(2)
        clear_screen()