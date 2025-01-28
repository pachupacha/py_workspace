import os
import time


def clear_screen():
    os.system("cls")


def vending_machine():

    products = {
        "1": {"name": "Water", "price": 10},
        "2": {"name": "Soda", "price": 15},
        "3": {"name": "Chips", "price": 12},
        "4": {"name": "Chocolate", "price": 20},
    }

    balance = 30
    cart = {}
    clear_screen()

    def view_cart():
        nonlocal balance

        while True:
            clear_screen()
            print("\n>>> YOUR CART <<<")
            total_spent = 0
            if cart:
                for idx, (item_name, item_data) in enumerate(cart.items(), start=1):
                    print(
                        f"{idx}- {item_name} x{item_data['count']} : ${item_data['total_price']}"
                    )
                    total_spent += item_data["total_price"]
                print(f"\n>>> Total in cart: ${total_spent} <<<")
            else:
                print("Your cart is empty.")

            print("\nOptions:")
            print("R. Remove a product")
            print("B. Back to main menu")
            print("Q. Checkout and exit")

            option = input("Choose an option (R/B/Q): ").strip().upper()

            if option == "R":
                if not cart:
                    print("\n>>> Your cart is empty. Nothing to remove. <<<")
                    time.sleep(2)
                else:
                    item_index = input(
                        "Enter the number of the product to remove: "
                    ).strip()
                    if item_index.isdigit():
                        item_index = int(item_index)
                        if 1 <= item_index <= len(cart):
                            item_name = list(cart.keys())[item_index - 1]

                            cart[item_name]["count"] -= 1
                            cart[item_name]["total_price"] -= products[
                                next(
                                    key
                                    for key, value in products.items()
                                    if value["name"] == item_name
                                )
                            ]["price"]

                            balance += products[
                                next(
                                    key
                                    for key, value in products.items()
                                    if value["name"] == item_name
                                )
                            ]["price"]

                            if cart[item_name]["count"] == 0:
                                del cart[item_name]

                            print(
                                f"\n>>> Removed one {item_name}. New balance: ${balance} <<<"
                            )
                            time.sleep(2)
                        else:
                            print("\n>>> Invalid product number. <<<")
                            time.sleep(2)
                    else:
                        print("\n>>> Please enter a valid number. <<<")
                        time.sleep(2)

            elif option == "B":
                break

            elif option == "Q":
                checkout()
                exit()

            else:
                print("\n>>> Invalid option. Please choose R, B, or Q. <<<")
                time.sleep(2)

    def checkout():
        clear_screen()
        print("\n>>> Thank you for using the vending machine! <<<")
        if cart:
            print("You purchased:")
            for item_name, item_data in cart.items():
                print(
                    f"- {item_name} x{item_data['count']} : ${item_data['total_price']}"
                )
        else:
            print("You didn't buy anything.")
        print(f"Remaining balance: ${balance}")
        time.sleep(2)

    while True:
        clear_screen()
        print("\nVENDING MACHINE 24/7\n")
        print("\nAvailable products:")
        for key, item in products.items():
            print(f"{key}. {item['name']} - ${item['price']}")

        print(f"\nYour current balance: ${balance}")
        print("5. Add balance")
        print("6. View cart")
        print("7. Checkout and exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice in products:
            product = products[choice]

            if balance >= product["price"]:
                if product["name"] in cart:
                    cart[product["name"]]["count"] += 1
                    cart[product["name"]]["total_price"] += product["price"]
                else:
                    cart[product["name"]] = {
                        "count": 1,
                        "total_price": product["price"],
                    }

                balance -= product["price"]
                print(
                    f"\n>>> You added {product['name']} to your cart. Remaining balance: ${balance} <<<"
                )
                time.sleep(2)
            else:
                print("\n>>> Insufficient balance. Please add more funds. <<<")
                time.sleep(2)

        elif choice == "5":
            amount = input("\nEnter the amount to add: ").strip()
            clear_screen()
            if amount.isdigit():
                balance += int(amount)
                print("\n")
                print(
                    f"\n>>> You added ${amount} to your balance. New balance: ${balance} <<<"
                )
                time.sleep(2)
            else:
                print("\n>>> Invalid amount. Please enter a number. <<<")
                time.sleep(2)

        elif choice == "6":
            view_cart()

        elif choice == "7":
            checkout()
            break

        else:
            print("\n>>> Invalid option. Please choose a number from 1 to 7. <<<")
            time.sleep(2)


vending_machine()