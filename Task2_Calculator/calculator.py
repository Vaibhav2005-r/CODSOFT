def addition(a,b):
    """Function to add two numbers"""
    return a + b
def subtraction(a,b):
    """Function to subtract two numbers"""
    return a - b
def multiplication(a,b):
    """Function to multiply two numbers"""
    return a * b
def division(a,b):
    """Function to divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
    if operation == 'exit':
        print("Exiting the calculator.")
        break
    elif operation == '+':
        print(f"{a} + {b} = {addition(a, b)}")
    elif operation == '-':
        print(f"{a} - {b} = {subtraction(a, b)}")
    elif operation == '*':
        print(f"{a} * {b} = {multiplication(a, b)}")
    elif operation == '/':
        try:
            print(f"{a} / {b} = {division(a, b)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation. Please try again.")

