import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_dungeon(size):
    dungeon = [[' ' for _ in range(size)] for _ in range(size)]
    player = (random.randint(0, size - 1), random.randint(0, size - 1))
    exit_door = (random.randint(0, size - 1), random.randint(0, size - 1))
    key = (random.randint(0, size - 1), random.randint(0, size - 1))
    
    while exit_door == player:
        exit_door = (random.randint(0, size - 1), random.randint(0, size - 1))
    while key == player or key == exit_door:
        key = (random.randint(0, size - 1), random.randint(0, size - 1))
    
    return dungeon, player, exit_door, key

def display_dungeon(dungeon, player, has_key, exit_door, key):
    clear_screen()
    for i in range(len(dungeon)):
        for j in range(len(dungeon[i])):
            if (i, j) == player:
                print('🧍', end=' ')
            elif (i, j) == exit_door:
                print('🚪', end=' ')
            elif (i, j) == key and not has_key:
                print('🔑', end=' ')
            else:
                print('⬜', end=' ')
        print()

def play():
    size = 5
    dungeon, player, exit_door, key = generate_dungeon(size)
    has_key = False
    moves = 15
    
    while moves > 0:
        display_dungeon(dungeon, player, has_key, exit_door, key)
        print(f"Remaining moves: {moves}")
        direction = input("Move (north, south, east, west): ").lower()
        
        x, y = player
        if direction == 'north' and x > 0:
            player = (x - 1, y)
        elif direction == 'south' and x < size - 1:
            player = (x + 1, y)
        elif direction == 'east' and y < size - 1:
            player = (x, y + 1)
        elif direction == 'west' and y > 0:
            player = (x, y - 1)
        else:
            print("Invalid move!")
            continue
        
        if player == key:
            has_key = True
            print("You picked up the key! 🔑")
        
        if player == exit_door:
            if has_key:
                print("You have escaped the dungeon! 🎉")
                return
            else:
                print("The door is locked, you need the key. 🔐")
        
        moves -= 1
    
    print("You ran out of moves! Game Over. ☠️")

if __name__ == "__main__":
    play()