# from abc import ABC,abstractmethod 

# class Person(ABC):

#     @abstractmethod  # This decorator marks the eating method as abstract method in Person abstract class.
#     def eating(self):
#         pass
# class Child(Person):
#     def eating(self):
#         print("he is eating")
#     def running(self):
#         print("this is child class")
 


# c1 = Child()
# c1.running()

# c1.eating() # This will give an error because eating method in Child class is not implemented.

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

# # Create an instance of the Hatchback class
# car1 = Hatchback("Maruti", "Alto", "2022")

# # Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()

s1 = Suv("honda",2022,2000)

s1.sunroof()