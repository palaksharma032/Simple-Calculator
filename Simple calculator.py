# Simple Calculator: Addition, Subtraction, Multiplication, and Division of two numbers
# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Addition
print(f"Addition of {num1} + {num2} is: {num1 + num2}")
# Subtraction (num1 - num2)
print(f"Subtraction of {num1} - {num2} is: {num1 - num2}")
# Subtraction (num2 - num1)
print(f"Subtraction of {num2} - {num1} is: {num2 - num1}")
# Multiplication
print(f"Multiplication of {num1} * {num2} is: {num1 * num2}")
# Division (num1 / num2)
if num2 != 0:
    print(f"Division of {num1} / {num2} is: {num1 / num2}")
else:
    print(f"Division of {num1} / {num2} is: Invalid (division by zero)")
# Division (num2 / num1)
if num1 != 0:
    print(f"Division of {num2} / {num1} is: {num2 / num1}")
else:
    print(f"Division of {num2} / {num1} is: Invalid (division by zero)")
