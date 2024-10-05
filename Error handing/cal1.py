
def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides two numbers and handles division by zero."""
    return x /   y

def mod(x, y):
    """This function calculates the modulus of two numbers."""
    return x % y

def exponent(x, y):
    """This function raises x to the power of y."""
    return x ** y


first_value = int(input( "write your first number : "))
second_value = int(input( "write your second number : "))
choice = input("choice what do you want to do : ( '+ , - , * , / , % , **'  ) : ")
if choice == "+":
    print(add(first_value,second_value))
elif choice == "*":
    print(multiply(first_value , second_value))
elif choice == "-":
    print(subtract(first_value, second_value))
elif choice == "/":
    print(divide(first_value, second_value))
elif choice == "%":
    print(mod(first_value, second_value))
elif choice == "**":
    print(exponent(first_value, second_value))
else :
    print("invalid choice")

print("uzair")

