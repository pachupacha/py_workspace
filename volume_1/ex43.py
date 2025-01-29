import os
import time
import random

def clear_screen():
    os.system("cls")

def generate_flight():
    airlines = ["Airways", "Skyline", "JetFly", "CloudAir", "EagleWings"]
    cities = ["New York", "London", "Tokyo", "Paris", "Berlin", "Sydney"]
    statuses = ["On Time", "Delayed", "Boarding", "Cancelled"]
    return {
        "flight": f"{random.choice(airlines)} {random.randint(100, 999)}",
        "destination": random.choice(cities),
        "time": f"{random.randint(0, 23):02}:{random.randint(0, 59):02}",
        "status": random.choice(statuses)
    }

def display_board():
    flights = [generate_flight() for _ in range(5)]
    while True:
        clear_screen()
        print("\n  AIRPORT FLIGHT INFORMATION  ")
        print("=" * 35)
        print(" FLIGHT   | DESTINATION | TIME  | STATUS  ")
        print("=" * 35)
        for flight in flights:
            print(f" {flight['flight']:8} | {flight['destination']:10} | {flight['time']:5} | {flight['status']:8} ")
        print("=" * 35)
        time.sleep(3)
        flights[random.randint(0, 4)] = generate_flight()

display_board()