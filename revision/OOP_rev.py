# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#     def eat(self,meal):
#         print(f"{self.name} is eating {meal}")
#     def bark(self):
#         print(f"{self.name} is barking")
#     def sleep(self):
#         print(f"{self.name} is sleeping")



print("uzair")


# # d1  = Dog("tommy" , "German" , 5)

# # print(d1.name)

# # print(d1.breed)

# # print(d1.age)

# # d1.eat("dog food")
# # d1.bark()
# # d1.sleep()

# # print()
# # d2 = Dog("Jack" , "Russian" ,6)

# # d2.eat("cat food")
# # d2.bark()
# # d2.sleep()
# # print(d2.name)

# # print(d2.breed)

# # print(d2.age)



# # inheritance
# class GrandFather:
#     def guide_g(self):
#         print("Father is guiding you")
#     def work_g(self):
#         print("Father is working")
# class Father:
#     def guide(self):
#         print("Father is guiding you")
#     def work(self):
#         print("Father is working")
# class Mother(Father):
#     def protect(self):
#         print("Mother is protecting you")
#     def cook(self):
#         print("Mother is cooking")

# class Child(Mother):
#     def play(self):
#         print("Child is playing")
#     def eat(self):
#         print("Child is eating")

# class Child2(Child,GrandFather):
#     def play2(self):
#         print("Child is playing")
#     def eat2(self):
#         print("Child is eating")
# c1 = Child()

# c1.play()
# c1.eat()
# c1.cook()
# c1.guide()


# # m1 = Mother()

# # m1.protect()
# # m1.cook()

# # m1.guide()




# Encapsulation 
# class Dog:
#     def __init__(self, name, breed, age):
#         self.__name = name
#         self.__breed = breed
#         self.__age = age
#     def __eat(self,meal):
#         print(f"{self.__name} is eating {meal}")
#     def __bark(self):
#         print(f"{self.__name} is barking")
#     def __sleep(self):
#         print(f"{self.__name} is sleeping")
#     def admin(self):
#         return self.__name,self.__breed,self.__age
    






# d1  = Dog("tommy" , "German" , 5)
# print(d1.admin())

# print(d1.__name)

# print(d1.__breed)

# print(d1.__age)

# d1.__eat("dog food")
# d1.__bark()
# d1.__sleep()

# print()
# d2 = Dog("Jack" , "Russian" ,6)

# d2.eat("cat food")
# d2.bark()
# d2.sleep()
# print(d2.name)

# print(d2.breed)

# print(d2.age)




# Polymorphism


# class Cal:

#     def add(self,a,b,c):
#         return a + b + c
# class Cal2(Cal):
#     def add(self,a,b):
#         return a + b
    



# c1=Cal()
# c2 = Cal2()


# print(c1.add(1,2,3))

# print(c2.add(1,2))




# Abstraction

# from abc import ABC , abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#     def eat(self):
#         print("Some generic animal eating")
#     def sleep(self):
#         print("Some generic animal sleeping")

# class Dog(Animal):
#     def sound(self):
#         print("Woof")
#     def eat(self):
#         print("Dog eating")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")
#     def eat(self):
#         print("Cat eating")






# c1 = Cat()

# c1.eat()

# c1.sound()


# d1 =Dog()
# d1.sound()
# d1.eat()
