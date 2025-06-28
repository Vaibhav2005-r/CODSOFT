from word2number import w2n
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
        a = (input("Enter first number: "))
        if a.is_float():
            a = float(a)
        else:
            a = w2n.word_to_num(a) 
        b = (input("Enter second number: "))
        if b.is_float():
            b = float(b)
        else:
            b = w2n.word_to_num(b)
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
