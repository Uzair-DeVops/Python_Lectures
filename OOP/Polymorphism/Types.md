# Types
# 1.Compile-time Polymorphism (Method Overloading)

**Compile-time polymorphism**, commonly referred to as **method overloading**, occurs when multiple methods in the same class have the same name but differ in the type or number of their parameters. The method to be executed is determined at compile time based on the method signature.

### Key Points about Method Overloading:
- **Same Method Name**: Multiple methods share the same name.
- **Different Parameters**: They differ in the number of parameters or the types of parameters.
- **Single Class**: Method overloading is implemented within a single class.
- **Static Binding**: The method call is resolved at compile time.

### Example of Method Overloading

Let's illustrate method overloading with a simple `Calculator` class that can add different types of numbers:

```python
class Calculator:
    # Method to add two integers
    def add(self, a: int, b: int) -> int:
        return a + b

    # Method to add three integers
    def add(self, a: int, b: int, c: int) -> int:
        return a + b + c

    # Method to add two floating-point numbers
    def add(self, a: float, b: float) -> float:
        return a + b

# Using the Calculator
calc = Calculator()

# These calls would raise an error because the last defined 'add' method will overwrite the previous ones.
# Uncommenting the following lines will raise errors.
# print(calc.add(5, 10))       # Error: TypeError, no matching method
# print(calc.add(5, 10, 15))   # This would work if the first definition were still there
# print(calc.add(5.5, 2.5))    # This would also work if the floating point version were the last defined.

```

### Note:
In Python, unlike languages like C++ or Java, method overloading does not work as expected because the last defined method with the same name overrides the previous ones. 

### Alternative to Method Overloading in Python

You can achieve similar functionality using default arguments or variable-length arguments:

#### Using Default Arguments

```python
class Calculator:
    # Method to add numbers with default parameters
    def add(self, a: int, b: int = 0, c: int = 0) -> int:
        return a + b + c

calc = Calculator()
print(calc.add(5))          # Output: 5 (only 'a' is provided)
print(calc.add(5, 10))      # Output: 15 ('a' and 'b' are provided)
print(calc.add(5, 10, 15))  # Output: 30 (all parameters are provided)
```

#### Using Variable-length Arguments

```python
class Calculator:
    # Method to add an arbitrary number of numbers
    def add(self, *args) -> int:
        return sum(args)

calc = Calculator()
print(calc.add(5))                # Output: 5
print(calc.add(5, 10))            # Output: 15
print(calc.add(5, 10, 15))        # Output: 30
print(calc.add(1, 2, 3, 4, 5))    # Output: 15 (can take any number of arguments)
```

### Summary
- **Compile-time Polymorphism** (Method Overloading) is a technique that allows the same method name to perform different tasks based on its parameters.
- Python does not support traditional method overloading but provides alternative ways to achieve similar results using default parameters or variable-length arguments.



# 2. Runtime Polymorphism (Method Overriding)

**Runtime polymorphism**, commonly known as **method overriding**, occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method to be invoked is determined at runtime based on the object type, allowing the same method call to behave differently depending on the object that it is invoked on.

### Key Points about Method Overriding:
- **Same Method Name**: Both the superclass and the subclass have a method with the same name and signature.
- **Subclass Implementation**: The subclass provides its own implementation of the method.
- **Dynamic Binding**: The method call is resolved at runtime, which means the correct method is called based on the object type.

### Example of Method Overriding

Let's illustrate method overriding with a simple example involving a base class `Animal` and derived classes `Dog` and `Cat`:

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Create instances of Dog and Cat
animal1 = Dog()
animal2 = Cat()

# Call the sound method
animal1.sound()  # Output: Woof! Woof!
animal2.sound()  # Output: Meow!
```

### Explanation of the Example:
1. **Base Class**: The `Animal` class has a method `sound()` that prints a generic animal sound.
2. **Derived Classes**: The `Dog` and `Cat` classes override the `sound()` method to provide their specific implementations.
3. **Method Call**: When we call the `sound()` method on an instance of `Dog`, it invokes the overridden method in the `Dog` class. Similarly, for an instance of `Cat`, it invokes the method in the `Cat` class.

### Advantages of Runtime Polymorphism:
- **Flexibility**: You can use a unified interface (the base class) while providing specific implementations in derived classes.
- **Code Maintenance**: It enhances the maintainability of code by allowing changes to be made in derived classes without altering the base class.

### Real-Life Example

1. **Shape Area Calculation**:
   - **Base Class**: `Shape` with a method `area()`.
   - **Derived Classes**: `Circle` and `Rectangle`, each implementing the `area()` method to calculate the area based on their specific shapes.

```python
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create instances of Circle and Rectangle
shapes = [Circle(5), Rectangle(4, 6)]

# Calculate areas
for shape in shapes:
    print(f"Area: {shape.area()}")
```

**Output**:
```
Area: 78.53981633974483
Area: 24
```

### Summary
- **Runtime Polymorphism** (Method Overriding) allows subclasses to provide specific implementations for methods defined in their superclass.
- It promotes flexibility and maintainability in code design by enabling the same method to behave differently depending on the object type.