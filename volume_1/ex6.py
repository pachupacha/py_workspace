print("Restaurant ´The Galician´")


mixed_salad = input("Portions of Mixed Salad consumed at the table: ")
fish_soup = input("Portions of Fish Soup consumed at the table: ")
baked_sea_bream = input("Portions of Baked Sea Bream consumed at the table: ")
curry_rice = input("Portions of Curry Rice consumed at the table: ")
meat_lasagna = input("Portions of Meat Lasagna consumed at the table: ")
chocolate_brownie = input("Portions of Chocolate Brownie consumed at the table: ")
ice_cream = input("Portions of Ice Cream consumed at the table: ")
soft_drinks = input("Number of Soft Drinks consumed at the table: ")
coffee = input("Cups of Coffee consumed at the table: ")

price_mixed_salad = 12
price_fish_soup = 10
price_baked_sea_bream = 18
price_curry_rice = 14
price_meat_lasagna = 15
price_chocolate_brownie = 8
price_ice_cream = 6
price_soft_drinks = 5.5
price_coffee = 3.5

final_bill = (
      float(mixed_salad) * price_mixed_salad
    + float(fish_soup) * price_fish_soup
    + float(baked_sea_bream) * price_baked_sea_bream
    + float(curry_rice) * price_curry_rice
    + float(meat_lasagna) * price_meat_lasagna
    + float(chocolate_brownie) * price_chocolate_brownie
    + float(ice_cream) * price_ice_cream
    + float(soft_drinks) * price_soft_drinks
    + float(coffee) * price_coffee
)

print("Your total bill is: €" + str(final_bill))
