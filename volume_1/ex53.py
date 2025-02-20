import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_ball(pins_left):
    return random.randint(0, pins_left)

def play_turn():
    pins_left = 10
    roll1 = roll_ball(pins_left)
    if roll1 == 10:
        print("Strike! (X)")
        return (10, 0)
    pins_left -= roll1
    time.sleep(1)
    
    roll2 = roll_ball(pins_left)
    if roll1 + roll2 == 10:
        print("Spare! (/)")
    else:
        print(f"Roll 1: {roll1}, Roll 2: {roll2}")
    
    return (roll1, roll2)

def calculate_score(plays):
    total_score = 0
    for i in range(len(plays)):
        roll1, roll2 = plays[i]
        total_score += roll1 + roll2
        
        if roll1 == 10 and i < 9:  # Strike
            total_score += sum(plays[i+1])
            if plays[i+1][0] == 10 and i < 8:
                total_score += plays[i+2][0]
        elif roll1 + roll2 == 10 and i < 9:  # Spare
            total_score += plays[i+1][0]
    
    return total_score

def play_game():
    print("Welcome to the Bowling game.")
    input("Press ENTER to start")
    
    plays = []
    for frame in range(10):
        clear_screen()
        print(f"\nRound {frame + 1}")
        roll1, roll2 = play_turn()
        plays.append((roll1, roll2))
        time.sleep(2)
    
    score = calculate_score(plays)
    print("\nGame over! Final score:", score)

if __name__ == "__main__":
    play_game()