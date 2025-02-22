import random

def get_flavors():
    return {
        "creamy": ["Dulce de leche", "American cream", "Sambayón", "Lemon mousse", "Sky cream"],
        "chocolates": ["Dark chocolate", "Chocolate with almonds", "White chocolate", "Marroc", "Nutella"],
        "fruity": ["Strawberry", "Mango", "Pineapple", "Passion fruit", "Forest fruits"],
        "others": ["Tiramisu", "Banana Split", "Cookies and Cream", "Mint chip", "Coconut"]
    }

def get_prices():
    return {100: 2.5, 250: 5, 500: 9, 750: 13, 1000: 16}  # Prices in dollars

def run_test():
    questions = {
        "1. Do you love the feeling of creamy ice cream melting in your mouth? (Y/N)": "creamy",
        "2. If you could choose, would you go for a homemade and artisanal dessert over an industrial one? (Y/N)": "creamy",
        "3. Does intense chocolate transport you to a special moment? (Y/N)": "chocolates",
        "4. Do you enjoy the combination of chocolate with ingredients like cookies or nuts? (Y/N)": "chocolates",
        "5. When you think of a refreshing ice cream, do you imagine fruity flavors like mango or passion fruit? (Y/N)": "fruity",
        "6. Do you prefer a light and fresh ice cream rather than a dense and sweet one? (Y/N)": "fruity",
        "7. If given a choice between a tropical smoothie and a coffee with cream, would you go for the smoothie? (Y/N)": "fruity",
        "8. Do you like trying different flavors with an exotic touch? (Y/N)": "others",
        "9. When you eat ice cream, do you love it when it has crunchy bits or surprising textures? (Y/N)": "others",
        "10. Do you prefer to mix several flavors in your ice cream rather than choosing just one? (Y/N)": "others"
    }
    responses = {"creamy": 0, "chocolates": 0, "fruity": 0, "others": 0}
    
    for question, category in questions.items():
        answer = input(question).strip().upper()
        if answer == "Y":
            responses[category] += 1
    
    sorted_categories = sorted(responses.items(), key=lambda x: x[1], reverse=True)
    selected_categories = [cat for cat, score in sorted_categories if score > 0][:2]
    return selected_categories

def choose_flavors(flavors, quantity):
    print("Here are the available flavors:")
    flavor_list = [f for category in flavors.values() for f in category]
    for i, flavor in enumerate(flavor_list, 1):
        print(f"{i}. {flavor}")
    
    choices = []
    while len(choices) < quantity:
        try:
            option = input(f"Choose a flavor ({len(choices) + 1}/{quantity}) or type 'done' to finish early: ").strip()
            if option.lower() == "done" and choices:
                print(f"You have chosen fewer flavors. Your selection: {', '.join(choices)}")
                return choices
            option = int(option) - 1
            if 0 <= option < len(flavor_list) and flavor_list[option] not in choices:
                choices.append(flavor_list[option])
            else:
                print("Invalid or repeated selection. Try again.")
        except ValueError:
            print("Enter a valid number or type 'done' to finish early.")
    
    return choices

def main():
    print("Welcome to the ice cream shop!")
    prices = get_prices()
    total_price = 0
    order = []
    
    while True:
        quantity = int(input("How many grams do you want? (250, 500, 750, 1000) or enter 100 for a cone: "))
        if quantity not in prices:
            print("Invalid quantity, please try again.")
            continue
        
        allowed_flavors = {100: 2, 250: 2, 500: 3, 750: 3, 1000: 4}[quantity]
        flavors = get_flavors()
        
        if input("Would you like to take a test to choose flavors? (Y/N): ").strip().upper() == "Y":
            recommended_categories = run_test()
            suggested = []
            for category in recommended_categories:
                suggested += random.sample(flavors[category], min(allowed_flavors - len(suggested), len(flavors[category])))
                if len(suggested) >= allowed_flavors:
                    break
            print(f"We recommend these flavors: {', '.join(suggested)}")
            if input("Would you like to accept this recommendation? (Y/N): ").strip().upper() == "Y":
                order.append((quantity, suggested))
            else:
                print("Let's select the flavors manually.")
                choices = choose_flavors(flavors, allowed_flavors)
                order.append((quantity, choices))
        else:
            choices = choose_flavors(flavors, allowed_flavors)
            order.append((quantity, choices))
        
        total_price += prices[quantity]
        
        if input("Would you like to add more ice cream? (Y/N): ").strip().upper() != "Y":
            break
    
    print("\nFinal Receipt:")
    for q, flavors in order:
        print(f"{q}g: {', '.join(flavors)} - ${prices[q]:.2f}")
    print(f"Total price: ${total_price:.2f}")
    print("Thank you for your purchase!")

if __name__ == "__main__":
    main()