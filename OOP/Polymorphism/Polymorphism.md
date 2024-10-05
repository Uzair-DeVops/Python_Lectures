
# What is Polymorphism

The word **polymorphism** means having many forms. In programming, polymorphism refers to the ability to use the same function name (but with different signatures) for different types.

The term Polymorphism  means "many forms," and it allows methods to perform different tasks based on the object that it is acting upon

## Example of Inbuilt Polymorphic Functions

```python
# Python program to demonstrate in-built polymorphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))
```

**Output:**
```
5
3
```

## Examples of User-Defined Polymorphic Functions

```python
# A simple Python function to demonstrate Polymorphism
def add(x, y, z=0):
    return x + y + z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))
```

**Output:**
```
5
9
```



```python
class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan.")

    def language(self):
        print("Urdu is the national language of Pakistan.")

    def type(self):
        print("Pakistan is a developing country.")

class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")

    def language(self):
        print("Bengali is the most widely spoken language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")

# Creating objects for each class
obj_pak = Pakistan()
obj_bangladesh = Bangladesh()

# Loop through the objects and call their methods
for country in (obj_pak, obj_bangladesh):
    country.capital()
    country.language()
    country.type()

```


<!-- 
### Types of Polymorphism

1. **Compile-time Polymorphism (Static Binding)**:
   - This type of polymorphism is resolved during compile time. It is achieved through method overloading or operator overloading.
   - **Method Overloading**: Multiple methods in the same class have the same name but different parameters (different signatures).

   **Example**:
   ```python
   class MathOperations:
       def add(self, a: int, b: int) -> int:
           return a + b

       def add(self, a: float, b: float) -> float:
           return a + b

   # Usage
   math_op = MathOperations()
   print(math_op.add(5, 3))       # Output: 8
   print(math_op.add(5.5, 2.5))   # Output: 8.0
   ```

2. **Run-time Polymorphism (Dynamic Binding)**:
   - This type of polymorphism is resolved during run time. It is primarily achieved through method overriding, where a derived class overrides a method from its base class.
   - **Method Overriding**: The derived class has a method with the same name and parameters as in the base class.

   **Example**:
   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Dog(Animal):
       def speak(self):
           return "Bark"

   class Cat(Animal):
       def speak(self):
           return "Meow"

   # Usage
   def make_animal_speak(animal: Animal):
       print(animal.speak())

   dog = Dog()
   cat = Cat()

   make_animal_speak(dog)  # Output: Bark
   make_animal_speak(cat)  # Output: Meow
   ```

### Key Features of Polymorphism

- **Flexibility**: Polymorphism provides flexibility in code. You can write code that works with objects of different types using the same interface.
- **Code Reusability**: It allows for more generic and reusable code. You can write functions that can operate on objects of various classes.
- **Maintainability**: It enhances the maintainability of the code, as you can add new classes with minimal changes to existing code.

### Real-Life Examples of Polymorphism

1. **Payment Methods**: 
   - A system that handles different payment methods (like credit card, PayPal, and bank transfer) can have a method called `process_payment()`. Each payment method can have its own implementation.
   ```python
   class Payment:
       def process_payment(self):
           raise NotImplementedError("This method should be overridden.")

   class CreditCardPayment(Payment):
       def process_payment(self):
           return "Processing credit card payment"

   class PayPalPayment(Payment):
       def process_payment(self):
           return "Processing PayPal payment"

   # Usage
   def handle_payment(payment: Payment):
       print(payment.process_payment())

   credit_payment = CreditCardPayment()
   paypal_payment = PayPalPayment()

   handle_payment(credit_payment)  # Output: Processing credit card payment
   handle_payment(paypal_payment)   # Output: Processing PayPal payment
   ```

2. **Shape Area Calculation**: 
   - A program that calculates the area for different shapes (like circle and rectangle) can use polymorphism to handle the `area()` method differently for each shape.
   ```python
   import math

   class Shape:
       def area(self):
           raise NotImplementedError("This method should be overridden.")

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return math.pi * self.radius ** 2

   class Rectangle(Shape):
       def __init__(self, width, height):
           self.width = width
           self.height = height

       def area(self):
           return self.width * self.height

   # Usage
   def calculate_area(shape: Shape):
       print(shape.area())

   circle = Circle(5)
   rectangle = Rectangle(4, 6)

   calculate_area(circle)      # Output: Area of circle
   calculate_area(rectangle)   # Output: Area of rectangle
   ```

These examples illustrate how polymorphism allows different classes to implement methods in a way that is appropriate for their specific context, enhancing code flexibility and reusability. -->