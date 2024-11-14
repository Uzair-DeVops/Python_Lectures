# print('''Someone said : 
# #       this is good''')


# # print("uzair", end=" word ")
# # print("yasin")


# # print("uzair" , "yasin","ali","ahmed" , sep=" _ " )


# print("Muhammad \"Uzair\" \'Yasin\'")
# print("\U0001F600")
# # ""
# name = "1"
# print(type(name))
# print('uzair "ali" ')
# print("uzair yasin 'rafay'")
# print('''uzair "ali" , 'rafay'
#       yasin''')

# # Escape sequences
# print("uzair \tyasin")

# print("uzair \nyasin")

# print("yasin\ruzair")
# print("uzair  \"yasin\"")


# Variables
# it is used to stores values or u can say it a container
# # 
# name = "uzair"

# print(name)

# Rules no to do
# no number at start
# no spaces
# no hiyhen
# no pre used words

# rule to do
# meaningful variables


# int and float variables

# num  = 5.5

# type_var = type(num)

# print(type_var)


# input func

# name = input("write your name : ")
# print("your name is " , name)


# age = input("write your age : ")
# print("your age is " , age)  
# # print(type(age))


# type casting


# # age = int(input("write your age : "))
# # print("your age is " , age)  
# # print(type(age))

# #list to dic

# li = [1,2,3,4]
# dict = {}
# for x,y in enumerate(li):
#     dict[x]  = y


# print(dict)

# string to list

# name = "uzair"
# li = []
# for x in name:
#     li.append(x)

# print(li)

# # string to dictionary
# name = "uzair"

# dict = {}

# for x,y in enumerate(name):
#     dict[x]  = y

# print(dict)


# list to string

# li = ["u","z","a","i","r"]
# string_li = "".join(li)
# print(string_li)



# continue


# String

# anything inside a inverted commas is considered as a string

# name  = "my name is uzair and my age is 20"

# for x,y in enumerate(name):
#     print(f"{x} : {y}")

# syntax [start, end - 1,step]
# print(name[11:16: 2])

# reverse string
# print(name[::-1])


# string Func
# name  = "my name is uzair and my age is 20"

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.count("a"))
# print(name.find("a"))
# print(name.replace("a", "b"))
# print(name.split(" "))
# print(name.strip(" "))
# print(name.startswith("m"))
# print(name.endswith("0"))
# print(name.center(50,"*"))


# # If statement
# simple if
# marks = 50

# # if marks == 50:
#     print("Grade A")

# if else


# # if marks == 50:
#     print("Grade A")

# # else:
#     print("Grade B")


# if elif
# marks = 50

# if marks == 50:
#     print("Grade A")
# elif marks < 50:
#     print("Grade b")
# elif marks > 50:
#     print("Grade c")
# else:
#     print("Grade D")




# nested if

# marks = 50
# age = 20
# if marks == 50:
#     print("Grade A")
#     if age < 18:
#         print("You are eligible for driving")
#     else:
#         print("You are not eligible for driving")

# else:
#     print("Grade B")

    
# print("statement below if")


# for loop


# name = "uzair"

# simple loop
# for x in name:
#     print(x , end = "")

# range loop
# for x in range(0,11,2):
#     print(x)

# # nested loop
# for x in range(1,4):
#     for y in range(1,4):
#         print(x,y)



# while loop

# score = 0

# while score < 5:
#     print(score)
#     score += 1


# control statements


# score = 0

# while score < 5:
#     print(score)
#     score += 1
#     if score == 3:
#         continue



# for x in range(1,10):
#     if x == 6:
#         continue
#     else:
#         print(x)

# Functions
# def even_odd(x):
#     """This function is used to test whether a number is even or odd"""
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# for x in range(1,4):
#     even_odd(int(input("write any number : " )))

# print(enumerate.__doc__)

# non Pre (multiple types values can b stored)

# List
# li = [1,4,2,3, "uzair"]



# List Functions

# li.append(6)
# print(li)
# li.insert(2,7)
# print(li)
# li.remove(4)
# print(li)
# li.pop(2)
# print(li)
# li.sort()
# print(li)
# li.reverse()
# print(li)
# li.clear()
# print(li)
# li.extend([6,7,8])
# print(li)
# index = li.index(4)
# print(index)
# li = [1,2,3,4 , "uzair",True, 5
# .count(4)
# print(li)
# li = [1,2,3,4 , "uzair",True, 5
# .copy()
# print(li)
# 


# Tuple 
# tu = (1,2,3,4,"string")

# print(tu[2:4:2])


# Tuple Function

# tu = (1,2,3,4,"string")

# tu.count(1)

# # print(tu.index(4))



# Dictionary

# dict = {"a" : "Uzair", "b" : 20 , "c" : "Bscs"}


# for x ,y in dict.items():
#     print(f"{x} : {y}")


# print(dict["b"])


# dict2  = {}


# dict2["a"] = 1
# dict2["b"] = 2
# dict2["c"] = 3
# dict2["d"] = 4

# print(dict2)


# Dict Functios
dict = {"a" : "Uzair", "b" : 20 , "c" : "bscs"}
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("a"))
# print(dict.get("e"))
# print(dict.setdefault("d","rafay"))
# print(dict)
# print(dict.update({"d":"ali"}))
# print(dict)
# print(dict.pop("a"))
# print(dict)
# print(dict.popitem())
# print(dict)



# Error Handling
try:
    age = int(input("write your age : "))
    print(age)
except Exception as e:
    print("error occurred")
else:
    print("No error occurred")
finally:
    print("done")

print("uzair")


