# # class Shape:
# #     def calculate_area(self, radius):
# #         return 3.14 * radius * radius  # Area of a circle

# #     def calculate_area(self, length, width = 1):
# #         return length * width  # Area of a rectangle

# # # Usage
# # shape = Shape()
# # circle_area = shape.calculate_area(10)  # This will give an error
# # rectangle_area = shape.calculate_area(5, 10)
# # print(f"Rectangle Area: {rectangle_area}")
# # print(circle_area)

# # class Pakistan():
# #     def capital(self):
# #         print("Islamabad is the capital of Pakistan.")

# #     def language(self):
# #         print("Urdu is the national language of Pakistan.")

# #     def type(self):
# #         print("Pakistan is a developing country.")

# # class Bangladesh():
# #     def capital(self):
# #         print("Dhaka is the capital of Bangladesh.")

# #     def language(self):
# #         print("Bengali is the most widely spoken language of Bangladesh.")

# #     def type(self):
# #         print("Bangladesh is a developing country.")

# # # Creating objects for each class
# # obj_pak = Pakistan()
# # obj_bangladesh = Bangladesh()

# # # Loop through the objects and call their methods
# # for country in (obj_pak, obj_bangladesh):
# #     country.capital()
# #     country.language()
# #     country.type()

# # class Pol:
# #     def add(self,*a):
# #         return sum(a)

    

# # over = Pol()
# # print(over.add(1))

# # # import random as  np
# # # vr = np.


# # # print(list.__base__)




# # class Person1:
# #     def running(self):
# #         print("Person1 is Running")
# #     def running(self):
# #         print("Person2 is Running")
# #     def running(self):
# #         print("Person3 is Running")



# # p1 = Person1()
# # p1.running()



# class Addition(object):
#     def add(self , x,y):
#         return x+y
#     def add(self, x,y,z):
#         return x + y + z
#     def add(self , a,b,c,d):
#         return a + b + c + d
#     # def add(self , *a):
#     #     return sum(a)


# a1 = Addition()
# print(a1.add(2))


class Animal:
    def sound(self):
        print("Some generic animal sound")
    def eat(self):
        print("Some generic animal eating")



class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

a1 = Animal()
a2 = Dog()
a2.sound()
a3 = Cat()






# class Credit:
#     def payment(self):
#         print("Payment is done by credit")
# class Paypal:
#     def payment(self):
#         print("Payment is done by paypal")
        

