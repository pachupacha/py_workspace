def calculate_bmi(weight, height):
    height_meters = height / 100  # Convert cm to meters
    return weight / (height_meters ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif 30.0 <= bmi <= 34.9:
        return "Obesity I"
    elif 35.0 <= bmi <= 39.9:
        return "Obesity II"
    elif 40.0 <= bmi <= 49.9:
        return "Obesity III"
    else:
        return "Obesity IV"

foods = {
    "Apple": 52,
    "Banana": 89,
    "Chicken": 165,
    "Rice": 130,
    "Bread": 265,
    "Fish": 206,
    "Eggs": 155,
    "Milk": 42,
    "Beans": 140,
    "Carrot": 41,
    "Broccoli": 55,
    "Orange": 47,
    "Strawberries": 32
}

def generate_diet(bmi):
    if bmi < 18.5:
        return {"Breakfast": ["Rice", "Milk"], "Lunch": ["Chicken", "Bread"], "Dinner": ["Eggs", "Banana"]}
    elif 18.5 <= bmi <= 24.9:
        return {"Breakfast": ["Strawberries", "Milk"], "Lunch": ["Fish", "Carrot"], "Dinner": ["Beans", "Broccoli"]}
    elif 25.0 <= bmi <= 29.9:
        return {"Breakfast": ["Orange", "Eggs"], "Lunch": ["Fish", "Broccoli"], "Dinner": ["Carrot", "Milk"]}
    else:
        return {"Breakfast": ["Apple", "Carrot"], "Lunch": ["Fish", "Broccoli"], "Dinner": ["Beans", "Orange"]}

def calculate_calories(diet):
    return sum(foods[food] for meal in diet.values() for food in meal if food in foods)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
ideal_weight = float(input("Enter your ideal weight in kg: "))

caloric_deficit = (weight - ideal_weight) * 7700

bmr = 1400 if weight < 80 else 1800
days_needed = caloric_deficit / 500 if caloric_deficit > 0 else 0
weeks_needed = days_needed / 7

bmr_calories = calculate_calories(diet := generate_diet(calculate_bmi(weight, height)))

print(f"\nYour BMI is: {calculate_bmi(weight, height):.2f} ({classify_bmi(calculate_bmi(weight, height))})")
print("Recommended diet:")
for meal, food_list in diet.items():
    print(f"{meal}: {', '.join(food_list)}")
print(f"Estimated daily calories: {bmr_calories} kcal")
print(f"Estimated time to reach ideal weight: {days_needed:.1f} days ({weeks_needed:.1f} weeks)")