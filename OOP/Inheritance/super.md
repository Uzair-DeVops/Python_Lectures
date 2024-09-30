Sure! Let’s break down the use of `super()` in simple terms.

### What is `super()`?

`super()` is a built-in function in Python that helps you call methods from a parent class. When you have a class that is based on another class (called inheritance), you can use `super()` to access the parent class's methods and properties.

### Why Do We Use `super()`?

1. **Calling Parent Methods**: If you want to use a method from the parent class in the child class, you can use `super()`. It allows you to call that method without having to mention the parent class's name.

2. **Making Code Cleaner**: If you change the name of the parent class later, using `super()` means you don’t have to go through all the child classes to change the name. It keeps your code tidy.

3. **Handling Multiple Inheritance**: Sometimes, a class can inherit from more than one class. `super()` helps Python figure out which method to call next, so you don’t have to worry about the order.

4. **Reusing Code**: By using `super()`, you can call methods from the parent class and then add more features in the child class. This saves you from rewriting the same code.

5. **Easier Initialization**: When creating an object (like a new dog or a new employee), `super()` helps make sure that the parent class’s properties are set up correctly.
```python
# INHERITANCE 

# A Python program to demonstrate inheritance
class Person(object):
  
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)




class Emp(Person):
  def __init__(self, name, id ,salary):
    super().__init__(name, id)
    self.salary = salary

  def display_info(self):
    super().Display()
    print(self.salary)
    
# Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

Emp_details = Emp("Mayank", 103,5000)

# calling parent class function
Emp_details.display_info()

# Calling child class function
# Emp_details.Print()
```
