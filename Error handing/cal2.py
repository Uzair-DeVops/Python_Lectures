def add(x, y):
    """This function adds two numbers but does not allow negative numbers."""
    try:
        if x < 0 or y < 0:
            raise ValueError("Error: Negative numbers are not allowed in addition.")
        return x + y
    except ValueError as e:
        return e

 
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides two numbers and handles division by zero."""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def mod(x, y):
    """This function calculates the modulus of two numbers."""
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Modulus by zero is not allowed."

def exponent(x, y):
    """This function raises x to the power of y."""
    return x ** y

try:
    first_value = int(input("Write your first number: "))
    second_value = int(input("Write your second number: "))
    choice = input("Choose what you want to do ( '+ , - , * , / , % , **'  ): ")

    if choice == "+":
        print(add(first_value, second_value))
    elif choice == "*":
        print(multiply(first_value, second_value))
    elif choice == "-":
        print(subtract(first_value, second_value))
    elif choice == "/":
        print(divide(first_value, second_value))
    elif choice == "%":
        print(mod(first_value, second_value))
    elif choice == "**":
        print(exponent(first_value, second_value))
    else:
        print("Invalid choice.")
except ValueError:
    print("Error: Please enter valid numbers.")


print("uzair")
