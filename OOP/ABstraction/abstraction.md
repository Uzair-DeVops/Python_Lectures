
# Data Abstraction in Python

**Last Updated**: 04 Jul, 2024

Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details from the user and show the details that are relevant to the users. For example, the readers of geeksforgeeks only know that a writer can write an article on geeksforgeeks, and when it gets published readers can read the articles but the reader is not aware of the background process of publishing the article.

A simple example of this can be a car. A car has an accelerator, clutch, and brake and we all know that pressing an accelerator will increase the speed of the car and applying the brake can stop the car but we don’t know the internal mechanism of the car and how these functionalities can work. This detail hiding is known as data abstraction.

To understand data abstraction we should be aware of the below basic concepts:

- OOP concepts in Python
- Classes in Python
- Abstract classes in Python

## Importance of Data Abstraction

It enables programmers to hide complex implementation details while just showing users the most crucial data and functions. This abstraction makes it easier to design modular and well-organized code, makes it simpler to understand and maintain, promotes code reuse, and improves developer collaboration.

## Data Abstraction in Python

Data abstraction in Python is a programming concept that hides complex implementation details while exposing only essential information and functionalities to users. In Python, we can achieve data abstraction by using abstract classes, and abstract classes can be created using the `abc` (abstract base class) module and `abstractmethod` of `abc` module.

### Abstraction Classes in Python

An abstract class is a class in which one or more abstract methods are defined. When a method is declared inside the class without its implementation, it is known as an abstract method.

- **Abstract Method**: In Python, the abstract method feature is not a default feature. To create an abstract method and abstract classes, we have to import the `ABC` and `abstractmethod` classes from the `abc` (Abstract Base Class) library. The abstract method of the base class forces its child class to implement all abstract methods defined in the base class. If we do not implement the abstract methods of the base class in the child class, our code will give an error. In the code below, `method_1` is an abstract method created using the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
        # empty body
        pass
```

- **Concrete Method**: Concrete methods are the methods defined in an abstract base class with their complete implementation. Concrete methods are required to avoid replication of code in subclasses. For example, in an abstract base class, there may be a method whose implementation is the same in all its subclasses, so we write the implementation of that method in the abstract base class. Afterward, we do not need to write the implementation of the concrete method again in every subclass. In the code below, `startEngine` is a concrete method.

```python
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")
```

### Steps to Create Abstract Base Class and Abstract Method:

1. Import `ABC` and `abstractmethod` class from the `abc` (Abstract Base Class) library.
2. Create a `BaseClass` that inherits from the `ABC` class. In Python, when a class inherits from `ABC`, it indicates that the class is intended to be an abstract base class.
3. Inside `BaseClass`, declare an abstract method named `method_1` by using the `abstractmethod` decorator. Any subclass derived from `BaseClass` must implement this `method_1` method. We write `pass` in this method, which indicates that there is no code or logic in this method.

```python
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
        # empty body
        pass
```

### Implementation of Data Abstraction in Python

In the code below, we have implemented data abstraction using an abstract class and method. Firstly, we import the required modules or classes from the `abc` library, then we create a base class `Car` that inherits from the `ABC` class that we have imported. Inside the base class, we create an `__init__` function, abstract function, and non-abstract functions. To declare the abstract function `printDetails`, we use the `@abstractmethod` decorator. After that, we create child classes `Hatchback` and `Suv`. Since these child classes inherit from the abstract class, we need to implement all abstract functions declared in the base class. We write the implementation of the abstract method in both child classes. We create an instance of a child class and call the `printDetails` method. In this way, we can achieve data abstraction.

```python
# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()
```

**Output**:
```
Brand: Maruti
Model: Alto
Year: 2022
Speed up ...
```
```python
from abc import ABC, abstractmethod

# Abstract class representing an ATM
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass
    
    @abstractmethod
    def enter_pin(self):
        pass
    
    @abstractmethod
    def perform_transaction(self):
        pass
    
# Concrete class implementing ATM functionalities
class BankATM(ATM):
    def insert_card(self):
        print("Card inserted.")
        
    def enter_pin(self):
        print("PIN entered.")
    
    def perform_transaction(self):
        print("Transaction successful! Here is your cash.")

# Usage
atm = BankATM()
atm.insert_card()
atm.enter_pin()
atm.perform_transaction()
```
