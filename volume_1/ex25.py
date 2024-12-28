while True:
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        print("You must enter a valid age.")
        continue
    elif int(age_input) < 18 or int(age_input) > 100:
        print("You do not meet the age requirements for this analysis.")
        exit()
    break  

while True:
    income_per_mont = input("Enter your monthly net income: ")
    if not income_per_mont.isdigit():
        print("You must enter a valid amount.")
        continue
    elif float(income_per_mont) <= 1134:
        print("You must enter an amount greater than the minimum wage (€1134.00).")
        continue
    else:
        income = float(
            income_per_mont
        )  
        if income < 15000:
            taxing = income * 0.05
            print(
                f"Based on your monthly income of €{income:.2f}, you must pay 5% in taxes, totaling €{taxing:.2f}."
            )
        elif 15000 <= income <= 25000:
            taxing = income * 0.15
            print(
                f"Based on your monthly income of €{income:.2f}, you must pay 15% in taxes, totaling €{taxing:.2f}."
            )
        elif 25000 <= income <= 35000:
            taxing = income * 0.20
            print(
                f"Based on your monthly income of €{income:.2f}, you must pay 20% in taxes, totaling €{taxing:.2f}."
            )
        elif 35000 <= income <= 60000:
            taxing = income * 0.30
            print(
                f"Based on your monthly income of €{income:.2f}, you must pay 30% in taxes, totaling €{taxing:.2f}."
            )
        else:
            taxing = income * 0.45
            print(
                f"Based on your monthly income of €{income:.2f}, you must pay 45% in taxes, totaling €{taxing:.2f}."
            )
        break
