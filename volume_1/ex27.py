menu_items = ["Burger", "Fries", "Soda"]
menu_prices = [10.00, 5.00, 2.50]
order_items = []
order_quantities = []

print("Welcome to the restaurant!")
print("Menu:")
for i in range(len(menu_items)):
    print(f"{i + 1}. {menu_items[i]} - ${menu_prices[i]:.2f}")

while True:
    choice = input("\nEnter the number of the item you'd like to order (or 'done' to finish): ").strip()

    if choice.lower() == "done":
        break

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(menu_items):
            quantity = input(f"How many {menu_items[index]}s would you like? ").strip()
            if quantity.isdigit():
                order_items.append(menu_items[index])
                order_quantities.append(int(quantity))
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid choice. Please select a number from the menu.")
    else:
        print("Invalid input. Please enter a number or 'done'.")

print("\nOrder Summary:")
total = 0
for i in range(len(order_items)):
    item = order_items[i]
    quantity = order_quantities[i]
    price = menu_prices[menu_items.index(item)]
    subtotal = price * quantity
    total += subtotal
    print(f"{item} x{quantity}: ${subtotal:.2f}")

print(f"Total: ${total:.2f}")