euros = float(input("How many Euros do you want to exchange for Dollars? "))

exchange_rate = 1.2
dollars = euros * exchange_rate

conversion_fee = dollars * 0.10

final_amount = dollars - conversion_fee

print("\nTransaction Details\n")
print("Euro Amount: " + str(euros) + "€")
print("Dollars at the exchange rate of the day: USD " + str(dollars))
print("Exchange house fee: USD " + str(conversion_fee))
print("Final Amount: USD " + str(final_amount))