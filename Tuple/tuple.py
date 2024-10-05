# the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.

# We can find items in a tuple since finding any item does not make changes in the tuple.

# var = ("uzair", "for", "uzair")
# print(var)


# One cannot add items to a tuple once it is created. 
# Tuples cannot be appended or extended.
# We cannot remove items from a tuple once it is created. 




# Creating Python Tuples
# There are various ways by which you can create a tuple in Python. They are as follows:

# Using round brackets

# var : tuple[int | str | float , ...] = ( 2,3 ,8.5,"uzair", "for", "uzair")
# print(type(var))
# print(var)


# values : tuple[int | str , ... ] = (1,2,4,"uzair","rafay")

# print(values)


# With one item



# mytuple = ("uzair",)
# print(type(mytuple))
 
# #NOT a tuple
# mytuple : str = "uzair"
# print(type(mytuple))


# Tuple Constructor
# tu : tuple[int | str ,...] = (1,2,3,4,6 ,"uzair")
# print(tu)
# list1 = list(tu)
# print(list1)
# list1.append("ali")
# tu1 : tuple [int | str , ...] = tuple(list1)
# print(tu1)




# Different Operations Related to Tuples
# Below are the different operations related to tuples in Python:

# Concatenation

# a = "uzia"
# b = "iugd"
# print(a + b)

# # Code for concatenating 2 tuples
# tuple1 = (0, 1, 2, 3)
# tuple2 = ('python', 'uzair')
 
# # Concatenating above two
# result = (tuple1 + tuple2)
# print(result[0])

# # Nesting


# # Code for creating nested tuples
# tuple1 = (0, 1, 2, 3)
# tuple2 = ('python', 'uzair')
 
# tuple3 = (tuple1, tuple2)
# print(tuple3[0])
# # print(tuple3)


# # Repetition
# # Code to create a tuple with repetition
# tuple3 = ('python',"uzair")*5
# print(tuple3)

# Slicing
# tuple1 = (1,3,2,3,5,6,7,7,8,9,10)
# print(tuple1[::3])

# Deleting
# Code for deleting a tuple

# tuple3 = ( 0, 1)
 
# del tuple3
# print(tuple3)

# Finding the length
#  Code for printing the length of a tuple
# tuple2 = ('python', 'uzair')
# print(len(tuple2))

# Multiple Data Types with tuples


# tuple with different datatypes
# tuple_obj = ("immutable",True,23)
# print(tuple_obj)


# Conversion of lists to tuples


# tuple with different datatypes
# tuple_obj = ("immutable",True,23)
# print(tuple_obj)

# Tuples in a Loop


# list1 : list = [1,2,3,4,5]
# print(list1)
# tuple1 : tuple = tuple(list1)
# print(tuple1)


# li = []
# a = (2,3,4)
# b = (5,6,7)
# tu = (a + b)
# print(tu)
# print(tu.index(2))

# tuple1 = (0, 1, 2, 3)
# tuple2 = ('python', 'uzair')
 
# tuple3 = (tuple1, tuple2)
# print(tuple3[0])


# tuple3 = (1,) * 3
# print(tuple3)

# tu = (1,2,3,4,5,6,7)
# # 
# for x in tu:
#     print(x)
# def input_():
#     x = input( " number : ").split()
#     return x
# y = input_()
# print(int(y))
 

# def square_list(x,y):
#     for items in x:
#         h = items*2
#         y.appemd
#     print(x)

# li2 = []
# li = [1,2,3,4]
# square_list(li,li2)