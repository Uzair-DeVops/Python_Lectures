#   Output  
# print("Hello World")

#  Data types

# Primitive and Non primitive


# primitive  : u can store single value

# str : string : anything which comes inside inverted commas is called string
# int : integer : 123546846465468
# float : decimal number : 123.456
# bool : boolean : true/false

# type()

# print( type("5765") )

# ""
# ''
# '''''


# print(''' 'Quaid' Said : Work "Work" and Work ''')  
# print ('''uzair  
# yasin ''')

#  Escape Sequence 
# \n : new line
# \t : tab space
# \\ : back slash
# print(" 'Quaid' Said : Work \"Work\" and Work ")  
# print("uzair \nyasin")


#  Variables 

# name = 5.5
# print(name)
# Rules of Variable 

# no space 
# dont start with integer
# dont use special character
# dont use keyword


# meaningful name  
# a = 0
# print = "uzair"
# print(print)

# stages 

# 1. declaration
# 2. initialization

# name = "uzair" 


# String 
# indexing
# slicing 
# steping
#  [start : end : step]
# for reversing string we can give step in minus 
# name = "My name is Muhammad Uzair and I am a Piaic Student"
# print(name[::])

# immutable  : anything which is unchangeable
# mutable  : anything which is changeable


# String function 
# 1. lower()
# 2. upper()
# 3. title()
# 4. capitalize()


# name = "uzaira"
# Second_str = "" .join("uzair")
# # print(name)
# print(Second_str)

# print("uzair","yasin" , sep="-") 
# print("Yasin ")

# print("Hello", "World")
# num = False
# print(type(num))




# If statement

# i = 10

# if (i < 15):
#     print("true")
#     if (i != 10):
#         print("nested")
#     else:
#         print("c false")
# else:
#     print("P false")

# print("I am Not in if")4


# i = 10
# if (i != 10):
#     print("i is")
# else:
#     print("i is not")



# print("outside if")



# i = 25
# if (i == 10):
#     print("i is 10")
# elif (i == 25):
#     print("i is 15")
# elif (i == 25):
#     print("i is 20")
# else:
#     print("i is not present")
# i = 10
# if (i != 10):
#     print("parent if ")
# #     if (i > 5):
# #         print("child if")
# #     else:
# #         print("child else")
# # else:
# #     print("parent else")


# i = 10 
# if(i == 10):
#     print("parent if ")
#     if(i < 5):
#         print("child if ")
#     else:
#         print("child else")
#         if(i >5):
#             print("childesh if")
# else:
#     print("parent else")


# grading

# mark > 90   so A grade
# mark > 80   so B grade
# mark > 70   so B+ grade
# mark > 60   so B- grade
# mark > 50   so C grade
# fail


# marks = int(input("Enter your marks : "))
# if marks > 90:
#     print("Grade A")
# elif marks > 80:
#     print("Grade B")
# elif marks  > 70:
#     print("Grade C")
# elif marks > 60:
#     print("Grade D")
# elif  marks > 50:
#     print("Grade E")
# else:
