import os


def clear_screen():
    os.system("cls")


while True:
    num = input("Input a number: ")
    if not num.isnumeric():
        print("Only numbers are valid. Try Again.")
        continue
    elif int(num) > 50 or int(num) < 1:
        print("Try a number between 1-50.")
        continue
    else:
        for i in range(1, int(num) + 1):
            print("*" * i + " " * (int(num) - i))
        for i in range(int(num) - 1, 0, -1):
            print("*" * i + " " * (int(num) - i))
            while True:
                retry = input("\nDo you want to retry? Y/N: ").lower
                if retry == "y":
                    continue
                elif retry == "n":
                    break
                else:
                    print("Input a valid Option.")
                    continue
    break
