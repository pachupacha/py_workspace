import time
import os

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        clear_screen()
        print(f"\n{' ' * ((os.get_terminal_size().columns - len(str(i)) - 20) // 2)}{i} seconds remaining.\n")
        time.sleep(1)
    clear_screen()
    print("\nTimer finished!\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_timer():
    print("\nWelcome to the countdown timer!\n")
    timer = int(input("Enter the timer duration in seconds: "))
    print("\nStarting the countdown...\n")
    countdown_timer(timer)
    
    decision = input("Do you want to start another timer? (yes/no): ").strip().lower()
    while decision == "yes":
        clear_screen()
        print("\nStarting a new timer...\n")
        timer = int(input("Enter the new timer duration in seconds: "))
        print("\nStarting the new countdown...\n")
        countdown_timer(timer)
        decision = input("Do you want to start another timer? (yes/no): ").strip().lower()

run_timer()



