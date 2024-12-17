side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
    print(f"Side 1: {side1}\nSide 2: {side2}\nSide 3: {side3}\nThe triangular structure of the roof can be built.")
else:
    print("The triangular structure of the roof CANNOT be built.")