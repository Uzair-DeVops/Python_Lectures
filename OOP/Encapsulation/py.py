# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.__name = name
# # #         self.__age = age



# # # p1 = Person("uzair" , 20)
# # # print(p1._Person__name
# # def decorator(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result + 1  # Incrementing the result by 1
# #     return wrapper

# # @decorator
# # def add(x, y):
# #     return x + y

# # # Test the function
# # print(add(2, 4))  # Output will be 7, since 2+4 = 6, and decorator adds 1


# class Mother:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def running(self):
#         print("Mother is running")
# class Father:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def running(self):
#         print("running")
# class Child(Mother, Father):
#     def __init__(self, name, age, mother_name, father_name):
#         super().__init__(name, age)
#         super().__init__(mother_name, father_name)
#         Father.running(self)



# c = Child("uzair", 20, "sadia", "shahid")
# c.running()


class Person:
    def __init__(self, name):
        self.__name = name
    def __running(self):
        print("running")

    # def setter(self):
    #     self.__name = "uzair"
    # def Admin(self):
    #      return self.__name
    


# p1 = Person("uzair")
# print(p1._Person__name)
# p1._Person__running()


# # print(p1.Admin())
# p1.__name = "ali"
# print(p1.__name)
# # # print(p1.Admin()) #uzair
# # # print(p1.age) #20



# i = True
# num = 0
# while(i):
#     print("uzair")
#     num += 1
#     if num == 4:
#        break

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __eat(self):
        print("eating")
    # def admin(self):
    #     return self._name, self._age
    def admin(self):
        return self.__name, self.__age





person = Person("uzair" , 20)
# print(person.admin())
print(person.__name)
# print(person.__age)

# person.__eat() 

# print(person.name)
# print(person.age)
# print(person.admin())
 