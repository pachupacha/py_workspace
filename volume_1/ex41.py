import datetime
import os
import time


def clear_screen():
    os.system('cls')

calendar = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
vendors = {"user1": "pass1", "user2": "pass2", "user3": "pass3", "user4": "pass4", "user5": "pass5"}
appliances = {"Fridge": 500, "Washer": 300, "Dryer": 400, "Oven": 600, "Microwave": 150}
bonuses = {"Fridge": 0.05, "Washer": 0.03, "Dryer": 0.04, "Oven": 0.06, "Microwave": 0.02}

sales_data = []

print("Enter the date (dd/mm/yyyy):")
date_input = input().strip()
day, month, year = map(int, date_input.split("/"))
weekday = datetime.date(year, month, day).weekday()
discount_day = calendar[weekday] in ["Tuesday", "Saturday"]
print(f"Today is {calendar[weekday]}.")
time.sleep(2)
clear_screen()

logged_in = False
while not logged_in:
    print("Enter username:")
    username = input().strip()
    clear_screen()
    print("Enter password:")
    password = input().strip()
    clear_screen()
    if username in vendors and vendors[username] == password:
        logged_in = True
        print("Login successful.")
        time.sleep(2)
        clear_screen()
    else:
        print("Invalid credentials. Try again.")
        time.sleep(2)
        clear_screen()

def calculate_discounted_price(price):
    return price * 0.95 if discount_day else price

def record_sale(vendor, appliance, quantity):
    for _ in range(quantity):
        sales_data.append((vendor, appliance, calculate_discounted_price(appliances[appliance])))

def calculate_summary():
    total_sales = 0
    total_bonus = 0
    for vendor, appliance, price in sales_data:
        total_sales += price
        total_bonus += price * bonuses[appliance]
    return total_sales, total_bonus

session_active = True
while session_active:
    print("Enter appliance sold or 'logout' to end session:")
    action = input().strip()
    time.sleep(2)
    clear_screen()
    if action == "logout":
        session_active = False
    elif action in appliances:
        print(f"Enter quantity of {action} sold:")
        quantity = input().strip()
        time.sleep(2)
        clear_screen()
        if quantity.isdigit() and int(quantity) > 0:
            record_sale(username, action, int(quantity))
            print(f"{quantity} {action}(s) recorded.")
            time.sleep(2)
            clear_screen()
        else:
            print("Invalid quantity. Try again.")
            time.sleep(2)
            clear_screen()
    else:
        print("Invalid appliance. Try again.")
        time.sleep(2)
        clear_screen()

total_sales, total_bonus = calculate_summary()
print("End of day summary:")
print(f"Total Sales: ${total_sales:.2f}")
print(f"Total Bonus: ${total_bonus:.2f}")
print("Session closed.")