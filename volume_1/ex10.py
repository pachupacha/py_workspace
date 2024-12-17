name = input("What's your name?: ")
print("Hello " + str(name) + "!")
per_hour_money = input("How much money do you earn per hour?: ")
worked_hours = input("How many hours have you worked this week?: ")
weekly_expenses = input("How much money do you spend weekly?: ")
weekly_salary = (float(per_hour_money) * float(worked_hours))
annual_salary = float(weekly_salary) * 52
annual_expenses = float(weekly_expenses) * 52
annual_savings = (float(annual_salary) - float(annual_expenses))
print("\n")
print(str(name) + ", you have annual earnings of: " + str(annual_salary) + " Euros.")
print(str(name) + ", you have annual expenses of: " + str(annual_expenses) + " Euros.")
print(str(name) + ", you have annual savings of: " + str(annual_savings) + " Euros.")