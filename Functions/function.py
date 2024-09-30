# # def even_odd(x):
# #     if x % 2 == 0:
# #       return "even" 
# #     else:
# #       return "odd"

# # print(even_odd(4))
# # # # for x in range(1,5):
# # # #    user_input = int(input(f"wrrite your {x} number"))
# # # print(even_odd(10)) 

# # # # def print ():
# # # #    pass

# # # print("hello")
   


# # # # even_odd(int(input("write number "))) 
# # # # even_odd(int(input("write number ")))
# # # # even_odd(int(input("write number ")))


# # # # print("")

# # # def fun():
# # #     print("Welcome to GFG")
# # #     print("Welcome to GFG")
# # #     print("Welcome to GFG")
# # #     print("Welcome to GFG")




# # # fun()
# # # fun()



# # # Here a,b are the parameters
# # # def sum(a : int, b : int ) -> int:
# # #     return a  + b
# # #     print(a+b)


  

# # # print(sum(8,9))


# # # def is_prime(n):
# # #     if n <= 1:
# # #         return False
# # #     for i in range(2, int((n ** 0.5))):
# # #         if n % i == 0:
# # #             return False
# # #     return True


# # # # print(is_prime(9))

# # # def myFun(**kwargs):
# # #     for key, value in kwargs.items():
# # #         print(f"{key} = {value}")


# # # # Driver code
# # # myFun(first='Geeks', mid='for', last='Geeks')

# # # def add(fir,a):
# # #     """Add two numbers"""
# # #     return f" {a + b}"

# # # # Driver code
# # # print(add(1,2))

# # def person_name(first_name , Second_name, age  ):
# #   print(f"this is your first name {first_name} This is your second name {Second_name} and my  age is {age}")
  
# # person_name( age = 20 ,Second_name="yasin" ,first_name= "uzair" )

# # # def sum(x,y):
# # #     return x + y

# # # print(sum(2,7))

# # # def add(*argv):
# # #     y = 0
# # #     for x in argv:
# # #         return y + = x
        

# # # # print(add(2,3,5))

# # def myFun(*argv):
# #     for items in argv:
# #         print(items)


# # myFun("uzair","yasin" ,20)


# def myFun(**kargv):
#     # print(kargv)
#     """This function is about key word arguments"""
#     for key, value in kargv.items():
#         print(f"{key} = {value}")



# myFun( first = "uzair", sec = "yasin" ,age = 20 )
# print(myFun.__doc__)

# # # class Car:
# # #     def __init__(self ,color,model,company,size):
# # #         self.color = color
# # #         self.model = model
# # #         self.company = company
# # #         self.size = size
# # #     def info(self):
# # #         print(f"this car is {self.color} color and its model is {self.model} it is a {self.size} size car and it is made by {self.company} company ")
    
# # #     def drive(self):
# # #         print("the car is driving")
# # #     def dance(self):
# # #         print("the car is dancing")
# # #     def song(self):
# # #         print("the car is singing a song")


# # # c1 = Car("red" ,2024,"Supra","4x4") 
# # # print(c1.color)
# # # c1.dance()
# # # c1.drive()
# # # c1.info()


# # # def add(x,y):
# # #     return x + y

# # count = 0
# # while count  == 0:
# #     print("while")
# #     count = count + 1


# # # x = 10
# # # y = 20
# # # summ = lambda x,y,z : x+y+z
# # # print(summ(10,18,16))

# # def div(x,y):
# #    return x/y

# # def even_odd(n):
# #     if n % 2 == 0 :
# #       return "even"  
# #     else:
# #       return "odd"


# # ans = div(10 , 2)
# # print(ans)
# # print(even_odd(ans))

# # list1 = []
 
# # for x in range(3):
# #    ans = even_odd(int(input("number :")))
# # print(ans)

# # if ans == "even" :
# #    list1.append(ans)
# # else:
# #    print(ans) 
# # print(list1)

# def add(x,y):
#     return x + y

# add = lambda x,y : x+y
# print(add(2,3))

# name = "uzair"
# li = list(name)
# li[2] = "h"
# str2 = "" .join(li)
# print(li)
# print(str2)
# name[2] = "h"
# print(name)