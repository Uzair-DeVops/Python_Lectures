# # class Car:
# #     def __init__(a ,color,model) :
# #         a.color = color
# #         a.model = model
        
# #     def drive(self):
# #         print("The car is driving")
# #     def loading(self):
#         # print("The car is loading")
class Dog:
    def __init__(self, breed, age,color):
        self.breed = breed
        self.age = age
        self.color = color
    def bark(self):
        print("The dog is barking")
    def sleep(self):
        print("The dog is sleeping")
    def eat(self,food):
        print("eating" ,food)


dog1 = Dog("Russian" ,5,"black")
dog2 = Dog("Jerman" ,2,"pinky")
dog3 = Dog("bulldog" ,7,"white")

print(dog1.age) 
print(dog1.color)
dog1.eat("fish")
dog1.sleep()

print()
print(dog2.age)
print(dog2.color)
print(dog2.breed)
dog2.eat("mutton")

# # li =[1,2,3]
# # li.append()
# # car1 = Car("red" , 2024)
# # print(car1.color)
# # print(car1.model)
# # print()
# # car2 = Car("white" , 2022)
# # print(car2.color)
# # print(car2.model)
# # print()
# # car3 = Car("black" , 2023)
# # print(car3.color)
# # print(car3.model)



# # car1 = Car()



# # car1.drive()
# # print(car1.color)
# # print(car1.model)
# # print(car1.C_Name)
# # car1.loading()

# # car2 = Car()
# # print(car2.color)
# # print(car2.model)
# print("""Welcome to Treasure Island.
#       Your mission is to find the treasure
#       You're at a cross road. Where do yopu want to go? """ )
# first_step=str(input('Type \"left\" or \"right\" \n'))
# if first_step.lower()=="left":
#      print("You've come top lake.There is island in the middle of the lake.")
#      second_step=str(input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n"))
#      if second_step.lower()=="wait":
#         print("You arrive at the island unharmed. There is a house with 3 doors.")
#         third_step=str(input("One \"red\", One \"yellow\" and one \"blue\". Which color do you choose? \n"))
#         if third_step.lower()=="red":
#             print("Its a room full of fire. Game Over.")
#         if third_step.lower()=="yellow":
#             print("You find the treasure! You Win!")
#         if third_step.lower()=="blue":
#              print("Game Over")      
#      if second_step.lower()=="swim":
# #          print("You get attacked by an angry trout. Game Over")    
# # if first_step.lower()=="right":
# #     print("You fell into a hole. Game Over.")



# class Car:
#     # class variable or static variable
#     tier = 4
#     def __init__(self,color,model,company_n):
#         # class instance or dynamic variable
#         self.color = color
#         self.model = model
#         self.company_n = company_n
#     def driving(self):
#         print("The car is driving")
#     def loading(self,material):
#         print(f"The car is loading {material}")
    




# Car1 = Car("red" , 2023,"honda")
# Car1.color = "yellow"
# Car1.model = 2022
# print(Car1.color)
# print(Car1.model)
# Car1.driving()
# Car1.loading("food")
# print()
# Car2 = Car("white" , 2022,"Tesla")
# print(Car2.color)
# Car2.driving()
# Car2.loading("mirrors")

# # print(Car1.tier)
# # print(Car2.tier)


# li = [1,2,3,4]
# li.append("1")

# class Car:
#         color = "red"
#         model = 2024
#         company_n = "Honda"


# car1 = Car()
# print(car1.color)
# print(car1.model)
# print(car1.company_n) 
# car2 = Car()
# print(car2.color)
# print(car2.model)
# print(car2.company_n)
