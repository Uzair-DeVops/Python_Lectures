# Encapsulation in Object-Oriented Programming (OOP)

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

To prevent accidental changes, an object’s variable can only be changed by an object’s method. These types of variables are known as **private variables**.


#### Key Points:
- **Private Variables**: These are variables that are only accessible within the class they are defined in. In Python, private variables are usually prefixed with double underscores (`__`).
- **Controlled Access**: Methods inside the class allow controlled access and modification of these private variables, ensuring that the data is not changed in unintended ways.

---


Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of all the sales. Now there may arise a situation when for some reason an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section. He will first have to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.

### Real-Life Example 1: Bank Account

Imagine a bank account. The account balance is sensitive information that you don't want everyone to modify. Encapsulation ensures that only authorized methods like deposit and withdraw can modify the balance.

#### Code Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner  # Private variable
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance

# Using the BankAccount class
account = BankAccount("John", 500)
account.deposit(200)  # Deposited 200. New balance: 700
account.withdraw(150)  # Withdrew 150. Remaining balance: 550
print(account.get_balance())  # Output: 550
```

#### Explanation:
- The `__balance` variable is private and cannot be modified directly.
- Methods like `deposit()` and `withdraw()` provide controlled access to modify the balance.

---

### Real-Life Example 2: Student Grades

Consider a system where student grades are stored. The grades should not be modified by anyone other than the teacher or administrator. Encapsulation ensures that only authorized functions can modify these grades.

#### Code Example:
```python
class Student:
    def __init__(self, name):
        self.__name = name  # Private variable
        self.__grades = []  # Private variable
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Invalid grade. Must be between 0 and 100.")
    
    def get_grades(self):
        return self.__grades

# Using the Student class
student = Student("Alice")
student.add_grade(85)  # Added grade: 85
student.add_grade(92)  # Added grade: 92
print(student.get_grades())  # Output: [85, 92]
```

#### Explanation:
- The `__grades` list is private and cannot be accessed directly.
- The `add_grade()` method provides a safe way to add valid grades, while `get_grades()` allows access to view the grades.

---

**Getters** and **setters** are methods used in object-oriented programming (OOP) to access and modify the private attributes of a class. They provide a way to encapsulate the internal state of an object while controlling how that state can be read or modified. Here’s a breakdown of what they are and how they work:

### Getters
- **Definition**: A **getter** is a method that retrieves the value of a private attribute. It allows access to the value of an attribute without directly exposing it.
- **Purpose**: Getters promote encapsulation by providing a controlled way to access private data. They can include additional logic, such as validation or logging, before returning the value.
- **Naming Convention**: Getters typically follow the naming convention of `get_attribute_name`.

#### Example of a Getter:
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter method
    def get_name(self):
        return self.__name

# Usage
person = Person("Alice")
print(person.get_name())  # Output: Alice
```

### Setters
- **Definition**: A **setter** is a method that sets or modifies the value of a private attribute. It allows you to change the value of an attribute while controlling the input.
- **Purpose**: Setters provide a controlled way to update private data. They can include validation logic to ensure the new value is valid before setting it.
- **Naming Convention**: Setters typically follow the naming convention of `set_attribute_name`.

#### Example of a Setter:
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name  # Set the new name
        else:
            raise ValueError("Name must be a non-empty string")

# Usage
person = Person("Alice")
print(person.get_name())  # Output: Alice

person.set_name("Bob")  # Change name to Bob
print(person.get_name())  # Output: Bob

# person.set_name("")  # This will raise ValueError
```

### Summary of Getters and Setters
- **Encapsulation**: Both getters and setters help in encapsulating data within classes.
- **Control**: They provide control over how attributes are accessed and modified.
- **Validation**: Setters can enforce validation rules when changing the value of attributes.
- **Maintainability**: Using getters and setters makes your code easier to maintain, as changes to how data is stored or validated can be made without changing the interface.

### Real-Life Examples
1. **Bank Account**: 
   - **Getter**: Retrieve the account balance.
   - **Setter**: Update the balance with validation to prevent negative amounts.
   
   ```python
   class BankAccount:
       def __init__(self, balance):
           self.__balance = balance  # Private attribute

       def get_balance(self):
           return self.__balance

       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount
           else:
               raise ValueError("Deposit amount must be positive.")

   # Usage
   account = BankAccount(1000)
   print(account.get_balance())  # Output: 1000
   account.deposit(500)
   print(account.get_balance())  # Output: 1500
   ```

2. **Employee Record**:
   - **Getter**: Retrieve the employee's ID.
   - **Setter**: Update the employee's name with validation to ensure it’s not empty.
   
   ```python
   class Employee:
       def __init__(self, employee_id, name):
           self.__employee_id = employee_id
           self.__name = name  # Private attribute

       def get_employee_id(self):
           return self.__employee_id

       def set_name(self, name):
           if name:
               self.__name = name
           else:
               raise ValueError("Name cannot be empty.")

   # Usage
   emp = Employee(101, "John Doe")
   print(emp.get_employee_id())  # Output: 101
   emp.set_name("Jane Doe")  # Change name to Jane Doe
   ```

These examples illustrate how getters and setters help manage access to object attributes while maintaining encapsulation and control over data.

### Protected Members in Python


**Protected members** (in C++ and Java) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 

To accomplish this in Python, follow the convention by prefixing the name of the member with a single underscore “_”. 

Although the protected variable can be accessed outside the class as well as in the derived class (and can also be modified in the derived class), it is customary (a convention, not a rule) to not access the protected member outside the class body.


### Example 1: Employee Class with Protected Member

In this example, we have an `Employee` class with a protected variable `_salary`, and we access it in a derived class `Manager`.

#### Code Example:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected member
    
    def show_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: {self._salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_manager_info(self):
        print(f"Manager Name: {self.name}, Salary: {self._salary}, Department: {self.department}")

# Creating an instance of Manager
manager = Manager("Alice", 75000, "HR")

# Accessing protected member inside the subclass
manager.show_manager_info()

# Accessing the protected member from outside the class (not recommended)
print(f"Protected Salary: {manager._salary}")  # Technically allowed, but against convention
```

#### Output:
```
Manager Name: Alice, Salary: 75000, Department: HR
Protected Salary: 75000
```

#### Explanation:
- The protected member `_salary` can be accessed within the subclass `Manager` and even outside the class using `manager._salary`. However, it is customary to avoid accessing such members from outside the class.

---

### Example 2: Vehicle Class with Protected Member

In this example, we demonstrate a `Vehicle` class with a protected variable `_fuel_capacity` and how it is accessed and modified in a derived class `Car`.

#### Code Example:
```python
class Vehicle:
    def __init__(self, make, fuel_capacity):
        self.make = make
        self._fuel_capacity = fuel_capacity  # Protected member
    
    def show_vehicle_info(self):
        print(f"Vehicle Make: {self.make}, Fuel Capacity: {self._fuel_capacity} liters")

class Car(Vehicle):
    def __init__(self, make, fuel_capacity, model):
        super().__init__(make, fuel_capacity)
        self.model = model

    def show_car_info(self):
        print(f"Car Model: {self.model}, Make: {self.make}, Fuel Capacity: {self._fuel_capacity} liters")

# Creating an instance of Car
car = Car("Toyota", 50, "Corolla")

# Accessing protected member inside the subclass
car.show_car_info()

# Accessing the protected member from outside the class (not recommended)
print(f"Protected Fuel Capacity: {car._fuel_capacity}")  # Technically allowed, but against convention
```

#### Output:
```
Car Model: Corolla, Make: Toyota, Fuel Capacity: 50 liters
Protected Fuel Capacity: 50 liters
```

#### Explanation:
- The protected member `_fuel_capacity` is used inside the derived class `Car` and can also be accessed outside the class using `car._fuel_capacity`, though it is against best practices to do so.

---

### Trying to Modify Protected Members

In both examples, we can modify the protected members from outside the class or within a subclass. While this is technically allowed, it is discouraged to modify them outside the class body.

#### Example:
```python
car._fuel_capacity = 60  # Modifying the protected member
print(f"Modified Fuel Capacity: {car._fuel_capacity}")  # Output: 60
```

Even though the protected member is accessible and modifiable, it breaks the convention of encapsulation when done outside the class or its subclasses.


### Private Members in Python

In Python, private members are intended to be accessed only within the class where they are defined, unlike protected members that can be accessed in derived classes. To declare a member as private, you use a double underscore (`__`) before its name. However, Python does allow access to private members through a feature called *name mangling*.

### Key Concept:
- Private members are not truly private but are prefixed with the class name to make accidental access harder.
- Private members are prefixed with a double underscore (`__`), which changes the name of the variable behind the scenes (name mangling).
- Accessing private members outside the class should generally be avoided.

### Example 1: Bank Account with Private Balance

In this example, we define a `BankAccount` class where the balance is a private member. We will try to access it directly, which will raise an error, and demonstrate how it can be accessed using name mangling.

#### Code Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private member

    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.__balance}")

# Creating an instance of BankAccount
account = BankAccount("John", 5000)

# Accessing private member from within the class
account.show_balance()

# Trying to access private member from outside the class (will raise an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

# Accessing private member using name mangling
print(account._BankAccount__balance)  # Accessing through name mangling
```

#### Output:
```
John's Balance: 5000
5000
```

#### Explanation:
- Accessing `__balance` directly outside the class raises an `AttributeError` because it is a private member.
- The private member can still be accessed using name mangling, which prefixes the class name to the private variable (`_BankAccount__balance`).

---

### Example 2: Employee Class with Private Salary

In this example, we create an `Employee` class with a private variable `__salary` and demonstrate the concept of name mangling when trying to access or modify the private variable.

#### Code Example:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private member

    def get_salary(self):
        return f"{self.name}'s Salary: {self.__salary}"

# Creating an instance of Employee
employee = Employee("Alice", 75000)

# Accessing private member from within the class
print(employee.get_salary())

# Trying to access private member directly (will raise an error)
# print(employee.__salary)  # Uncommenting this line will raise an AttributeError

# Accessing private member using name mangling
print(employee._Employee__salary)  # Accessing through name mangling
```

#### Output:
```
Alice's Salary: 75000
75000
```

#### Explanation:
- Direct access to `__salary` outside the class raises an `AttributeError`.
- Using name mangling (`_Employee__salary`), we can access the private variable, but this should be avoided in practice to respect the encapsulation.

---

### Trying to Modify Private Members

In both examples, private members can be accessed or modified using name mangling, but this practice goes against the concept of encapsulation.

#### Example:
```python
# Modifying private member using name mangling
account._BankAccount__balance = 10000
print(f"Modified Balance: {account._BankAccount__balance}")  # Output: 10000
```

While it is technically possible to access and modify private members this way, it is generally discouraged, as the goal of private members is to prevent unintended access or modification from outside the class.



### Difference Between Private Variables, Protected Members, and Private Members in Python

In Python, the distinction between **private** and **protected** members is primarily based on how the member variables and methods of a class are intended to be accessed or modified. Python provides special conventions for these types of members, but it doesn't enforce strict access restrictions like some other languages (e.g., Java, C++).

Here’s a breakdown of the differences:

---

### 1. **Private Variables**
- **Definition**: Private variables are those that are intended to be accessed and modified only within the class in which they are defined. These variables are marked by a **double underscore** (`__`) before their name.
- **Convention**: Use a double underscore (`__`) to declare a private variable. Python uses *name mangling* to change the name of the private variable, so it can't be accessed directly outside the class.
- **Access**: Only accessible inside the class or via name mangling outside the class.
- **Purpose**: To restrict access and prevent unintended modifications from outside the class, ensuring better encapsulation.

#### Example:
```python
class Car:
    def __init__(self, model, price):
        self.model = model
        self.__price = price  # Private variable

    def show_price(self):
        return f"The price of {self.model} is {self.__price}"

# Accessing within the class is fine
car = Car("Tesla", 50000)
print(car.show_price())

# Direct access outside the class raises an error
# print(car.__price)  # Raises AttributeError

# Access using name mangling
print(car._Car__price)  # Works, but against encapsulation principles
```

---

### 2. **Protected Members**
- **Definition**: Protected members are meant to be accessed within the class and subclasses. Python allows protected members to be accessed outside the class as well (though it's against convention). These are marked by a **single underscore** (`_`).
- **Convention**: Use a single underscore (`_`) before the member name to indicate that it is intended to be protected.
- **Access**: Can be accessed within the class and derived (subclass) classes. It's also accessible outside the class, but it’s considered improper practice to do so.
- **Purpose**: Protected members signal to developers that these members should not be accessed or modified directly outside the class, except in subclasses.

#### Example:
```python
class Animal:
    def __init__(self, species):
        self._species = species  # Protected member

    def get_species(self):
        return self._species

class Dog(Animal):
    def show_species(self):
        return f"I am a {self._species}"

# Accessing protected member within subclass
dog = Dog("Canine")
print(dog.show_species())  # Works fine

# Accessing outside the class is possible but discouraged
print(dog._species)  # Works, but it's against the convention
```

---

### 3. **Private Members**
- **Definition**: In Python, private members are similar to private variables, but the term is used more broadly to describe variables or methods intended to be accessed only within the class. These members are not supposed to be inherited or accessed by subclasses or outside the class.
- **Convention**: Private members are declared using **double underscores** (`__`).
- **Access**: Can only be accessed within the class where they are declared (or via name mangling). They are not intended to be inherited by subclasses.
- **Purpose**: To strictly hide the implementation details and ensure the internal workings of a class are shielded from external access.

#### Example:
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private member
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def __secret_method(self):  # Private method
        return "This is a private method"

# Accessing private members directly raises an error
account = BankAccount(12345, 1000)
# print(account.__balance)  # Raises AttributeError

# Access using name mangling
print(account._BankAccount__balance)  # Not recommended
```

---

### Summary of Differences:

| Type               | Prefix        | Intended Access                                 | Can be accessed outside class?        | Can be accessed in subclasses?  | Convention or Rule? |
|--------------------|---------------|-------------------------------------------------|--------------------------------------|---------------------------------|---------------------|
| **Private Variables** | `__` (double underscore) | Only inside the class; name mangling allows external access | **No**, except via name mangling    | **No**                             | Convention          |
| **Protected Members** | `_` (single underscore)  | Inside the class and its subclasses              | **Yes**, but discouraged (improper) | **Yes**                            | Convention          |
| **Private Members**   | `__` (double underscore) | Inside the class only, intended for internal use | **No**, except via name mangling    | **No**                             | Convention          |

---

In Python, the conventions around private and protected members are a way to indicate intent to other developers, rather than enforcing strict access control like some other languages.