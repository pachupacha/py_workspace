import os

def clear_screen():
    os.system('cls')

def convert_temperature(degrees, unit):
    if unit.lower() == 'c':
        return (degrees * 9/5) + 32
    elif unit.lower() == 'f':
        return (degrees - 32) * 5/9
    else:
        return None

clear_screen()

print("Temperature Converter")
degrees = float(input("Enter the temperature: "))
unit = input("Type 'C' for Celsius or 'F' for Fahrenheit: ")
result = convert_temperature(degrees, unit)

if result is not None:
    if unit.lower() == 'c':
        print(f"{degrees}°C is {result:.2f}°F")
    else:
        print(f"{degrees}°F is {result:.2f}°C")
else:
    print("Invalid unit. Please try again.")