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