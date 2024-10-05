# # original = {'a': [1, 2, 3], 'b': 100}
# # shallow_copy = original.copy()


# # # Modifying the original
# # original['a']="string"
# # print(original)      
# # print(shallow_copy)  

# # seq = ('a', 'b', 'c')
# # print(dict.fromkeys(seq,[1,2,3,4]))


# # # list1 = [1,2,3,4,5]
# # dic1 = {"a" : 1 , "b" : 2 , "c" : 3 , "d": 4 , "e" : 5 }
# # print(dic1)


# # Dict = {}
# # print("Empty Dictionary: ")
# # print(Dict)

# # list1 = [1,2,3,4,5]

# # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# # print("\nDictionary with the use of dict(): ")
# # print(Dict)

# # Dict = dict([(1, 'Geeks'), (2, 'For') ,(3, 'yes')])
# # print("\nDictionary with each item as a pair: ")
# # print(Dict)


# # list1 = [1,2,3,["A","B",[1,2,3],"C"],4,5]
# # # first = list1[3]
# # # sec = first[2]
# # # print(sec[1])

# # print(list1[3][2][1])


# # # Dict = {1: 'Geeks', 'name': 'For', 3: {"a" : 1 , "b" : 2}, 4 : {"c" : 1 , "d" : 2 , "e" : 5}}
# # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks' , 4 : (1,2,3)}
# # print(Dict.get)



# #  DELL()
# # Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# # print("Dictionary =")
# # print(Dict)
# # del(Dict["name"]) 
# # print("Data after deletion Dictionary=")
# # print(Dict)
# # del(Dict["name"]) 
# # print(Dict)


# # clear()
# # Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# # Dict2 = Dict.copy()
# # print(Dict)
# # print(Dict2)

# # fromkey()

# # seq = ('a', 'b', 'c')
# # Dict : dict = dict.fromkeys(())
# # print(Dict)
# # Dict["age"] = int(input("write any value : "))
# # Dict["gender"] = [input("write any value : ")]
# # Dict["name"] = (input("write any value : "),)
# # print(Dict)

# # pop()
# # Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# # Dict.pop(3)
# # print(Dict)
# #   
# # popitem()
# #  Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# # Dict.popitem()
# # print(Dict)
# #   
# # update()

# # Dictionary with three items
# # Dictionary1 = {'A': 'Geeks', 'B': 'For', }
# # Dictionary2 = {'B': 'Geeks' , "C" : "uzair"}

# # print("Original Dictionary:")
# # print(Dictionary1)
# # Dictionary1.update(Dictionary2)
# # print("Dictionary after updation:")
# # print(Dictionary1)


# # setdefault()
# my_dict = {'name': 'Alice', 'age':  25 ,'salary': 200 , "gender" : ""} 
# print(my_dict)

# # age = my_dict.setdefault('age', 10)
# # print(f"Age: {age}")  

# salary = my_dict.setdefault('salary', 50000)
# gender = my_dict.setdefault("gender","male")
# print(f"Salary: {salary}") 
# print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'salary': 50000}


# d = {'coding': 'good', 'thinking': 'better'}
# print(d['cod'])

# Python3 code to demonstrate 
# to initialize dictionary with list 
# using from keys()

# # using from keys() to construct
# new_dict = dict.fromkeys(range(4),)
	
# # printing result
# print ("New dictionary with empty lists as keys : " + str(new_dict))
# seq = ('a', 'b', 'c')
# print(dict.fromkeys(seq, None))
# seq = ('title', 'author', 'status')
# values = {}

# for key in seq:
#     user_input = input(f"Enter value for {key}: ")
#     values[key] = user_input

# print(values)
# value = {}
# value["a"] = "uzair"
# print(value)