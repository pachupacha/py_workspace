import time
import os


def burguer_selection():

    while True:
        burguer_input = input(
            "Welcome to Crispy Burguers.\nPlease, chose an Hamburguer (1-2):\n1.Classic Burguer\n2.Vegan Burguer\nOrder: "
        )
        if burguer_input == "1":
            os.system("cls")
            print("\n----------\nLet's Customize your Classic Burguer:\n----------\n")
            break
        elif burguer_input == "2":
            os.system("cls")
            print("\n----------\nLet's Customize your Vegan Burguer:\n----------\n")
            break
        else:
            os.system("cls")
            print(
                "\n----------\nPlease, insert a valid option. Select '1' or '2'.\n----------\n"
            )
            os.system("cls")
            continue
    time.sleep(1)
    os.system("cls")
    meat_count = 1
    vegan_meat_count = 1
    idiazabal_cheese_count = 0
    bacon_count = 0
    egg_count = 0
    tofu_count = 0
    caramelized_onion_count = 0

    if burguer_input == "1":
        print("Your Classic Burguer Includes:\n-Bread\n-Sazoned Meat x1\n")

        while True:
            print("Available Ingredients:\n")
            print(
                "1.Add Extra Meat x1 \n2.Add Idiazabal Cheese x1\n3.Add Bacon x1\n4.Add Fried Egg x1\n"
            )
            ingredient_input = input(
                "> Please, select your customization, or press '0' when you're finished.\n"
            )
            if ingredient_input == "0":
                break
            elif ingredient_input == "1":
                meat_count += 1
            elif ingredient_input == "2":
                idiazabal_cheese_count += 1
            elif ingredient_input == "3":
                bacon_count += 1
            elif ingredient_input == "4":
                egg_count += 1
            else:
                print("\n----------\nPlease chose a valid option.\n----------\n")
                continue
        print("\n----------\nYour classic Burguer is being prepared..\n----------\n")
        print("\nYour burguer includes: ")
        print(f"Meat x{meat_count}.")
        if idiazabal_cheese_count > 1:
            print(f"Idiazabal Cheese x{idiazabal_cheese_count}.")
        if bacon_count >= 1:
            print(f"Bacon x{bacon_count}.")
        if egg_count >= 1:
            print(f"Fried Egg x{egg_count}.")
        if idiazabal_cheese_count == 0 and bacon_count == 0 and egg_count == 0:
            print("No Additional Ingredients.")
        time.sleep(1)
        print("\n----------\nThanks for your order!\n----------\n")
    if burguer_input == "2":
        print("Your Vegan Burguer Includes:\n-Bread\n-Vegan Meat x1\n")

        while True:
            print("Available Ingredients:\n")
            print(
                "1.Add Extra Vegan Meat x1 \n2.Add Tofu x1\n3.Add Caramelized Onion x1\n"
            )
            ingredient_input = input(
                "> Please, select your customization, or press '0' when you're finished.\n"
            )
            if ingredient_input == "0":
                break
            elif ingredient_input == "1":
                vegan_meat_count += 1
            elif ingredient_input == "2":
                tofu_count += 1
            elif ingredient_input == "3":
                caramelized_onion_count += 1
            else:
                print("\n----------\nPlease chose a valid option.\n----------\n")
                continue
        print("\n----------\nYour classic Burguer is being prepared..\n----------\n")
        print("\nYour burguer includes: ")
        print(f"Vegan Meat x{vegan_meat_count}.")
        if tofu_count >= 1:
            print(f"Tofu x{tofu_count}.")
        if caramelized_onion_count >= 1:
            print(f"Caramelized Onion x{caramelized_onion_count}.")
        if tofu_count == 0 and caramelized_onion_count == 0:
            print("No Additional Ingredients.")
        time.sleep(1)
        print("\n----------\nThanks for your order!\n----------\n")


burguer_selection()
