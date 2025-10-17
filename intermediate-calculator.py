def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return a ** b
repeat = "yes"
while repeat == "yes":
    operation = input("Choose an operation (+, -, *, /, ^: ").strip()
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        if b != 0:
            result = divide(a, b)
        else:
            print("You cannot divide by zero.")
            continue 
    elif operation == "**":
        result = power(a, b)
    else:
        print("Invalid operation. Please try again.")
        continue 
    print("Result:", result)
    repeat = input("Do you want to run a new calculation? Enter yes to continue: ").lower()
print("Goodbye!")
