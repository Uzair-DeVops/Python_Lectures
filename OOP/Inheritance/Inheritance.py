# class GrandFather:

#   def Display_Gf(self):
#     print("this is father class")
#   def Wisdom(self):
#     print("this is guide method of Grand_father class")

    
# class Father(GrandFather):

#   def display_f(self):
#     print("this is father class")
#   def protect(self):
#     print("this is protect method of father class")

# class Son(Father):

#   def Print(self):
#     print("this is child class")
#   def Play(self):
#     print("this is play method of child class")


# class Son2(Father,GrandFather):
#   def Print(self):
#     print("this is child2 class")
#     def Play(self):
#       print("this is play method of child2 class")





# f1 = Father()
# print("father functions")
# f1.display_f()
# f1.protect()

# print()
# print("grandfather functions")
# f1.Display_Gf()
# f1.Wisdom()


# son1 = Son()
# son1.Play()

# print()
# print("father class functions")
# son1.display_f()

# print()
# print("grandfather class  functions")
# son1.Display_Gf()



# # # # e1= Son()
# # # # e1.Print()

# # # # print()
# # # # print("father functions")
# # # # e1.Display_f()
# # # # e1.Guide()

# # # # print()
# # # # print("mother functions")

# # # # e1.display_m()
# # # # e1.protect()


# # # class Animal:
# # #     def __init__(self, name):
# # #         self.name = name

# # # class Dog(Animal):
# # #     def __init__(self, name, breed):
# # #         super().__init__(name)
# # #   # Call the parent class's __init__
# # #         self.breed = breed


# # # dog1 =Dog("name" ,"any")
# # # print(dog1.name)  # Output: None
# # # print(dog1.breed)  # Output: None

# # class A:
# #     def process(self):
# #         print("Processing in A")

# # class B(A):
# #     def process(self):
# #         print("Processing in B")
# #         super().process()  # Call A's process method

# # class C(A):
# #     def process(self):
# #         print("Processing in C")
# #         super().process()  # Call A's process method

# # class D(B, C):
# #     def process(self):
# #         print("Processing in D")
# # #         super().process()  # This ensures B, C, and A are all called

# # # obj1=D()
# # # obj1.process()  # Output: Processing in D, Processing in B, Processing in C,






# # class Animal:
# #     def __init__(self, name):
# #         self.name = name

# #     def make_sound(self):
# #         print(f"{self.name} makes a generic animal sound.")


# # class Dog(Animal):
# #     def __init__(self, name, breed):
# #         super().__init__(name)  # Calls the parent class constructor
# #         self.breed = breed

# #     def make_sound(self):
# #         print(f"{self.name} barks.")
# #         super().make_sound()  # Calls the parent class method


# # dog = Dog("Buddy", "Golden Retriever")
# # dog.make_sound()


# class Father2:
#     def __init__(self, f_name, f_age):
#         self.f_name = f_name
#         self.f_age = f_age

#     def running(self):
#         print(f"This is running")

# class Child(Father2):
#     def __init__(self, f_name, f_age, my_name,my_grade):
#         super().__init__(f_name, f_age)
#         self.my_grade = my_grade
#         self.my_name = my_name
#     def running(self):
#         super().running()
   


# c1 = Child("yasin",55,"uzair","A")
# print(c1.f_name)
# print(c1.f_age)
# print(c1.my_name)
# print(c1.my_grade)
# c1.running()

# class Father:
#     def guide(self):
#         print("this is guide method of Father class")
#     def work(self):
#         print("this is work method of Father class")

# class Mother:
#     def protect(self):
#         print("this is protect method of Mother class")
#     def cook(self):
#         print("this is cook method of Mother class")




        
# class Children(Mother,Father):
#     def play(self):
#         print("this is play method of Children class")
#     def eat(self):
#         print("this is eat method of Children class")
#     def sleep(self):
#         print("this is sleep method of Children class")



# c1  = Children()
# print("\t\t\tthese are children class methods")
# c1.eat()
# c1.sleep()
# c1.play()

# print("\t\t\tthese are mother class methods")

# c1.protect()
# c1.cook()

# print("\t\t\tthese are father class methods")
# c1.work()
# c1.guide()

class Father:
    def guide(self):
        print("this is guide method of Father class")
    def work(self):
        print("this is work method of Father class")

class Mother(Father):
    def protect(self):
        print("this is protect method of Mother class")
    def cook(self):
        print("this is cook method of Mother class")

class Children1(Mother):
    def play(self):
        print("this is play method of Children class")
    def eat(self):
        print("this is eat method of Children class")
    def sleep(self):
        print("this is sleep method of Children class")

class Children2(Mother,Father):
    def play2(self):
        print("this is play method of Children class")
    def eat2(self):
        print("this is eat method of Children class")
    def sleep2(self):
        print("this is sleep method of Children class")


c1 = Children1()

c2 = Children2()

# c1  = Children()
# print("\t\t\tthese are children class methods")
# c1.eat()
# c1.sleep()
# c1.play()

# print("\t\t\tthese are mother class methods")

# c1.protect()
# c1.cook()

# print("\t\t\tthese are father class methods")
# c1.work()
# c1.guide()

# m1  = Mother()

# print("\t\t\tthese are mother class methods")

# m1.protect()

# m1.cook()

# m1.guide()

