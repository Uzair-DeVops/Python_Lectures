## Python list functions
## 1 . `Append()`
###  •	Description

Python list append function is a pre-defined function that takes a value as a parameter and adds it at the end of the list. append() function can take any type of data as input, including a number, a string, a decimal number, a list, or another object.
### •	Syntax 
It is very easy to use function you just need to call function with list object and passing value as parameter.

```
fruits : list = ["apple", "cherry", "banana"] 
fruits.append("grapes") 
print(fruits)

```
### •	Return Type None
 (This method only adds an element at the end of the list)


## 2 . `Extend()`
                                              
### •	Description
List extend() function is an in-built function of python that extends a list by adding values of an iterable (list,tuple,string) at the end of that list
### •	Syntax 
 ```
cars : list  = ["Audi","BMW","Jaguar"]
other_cars = ["Maruti", "Tata"]
cars.extend(other_cars)
print(cars)
 ```
### •	Return Type None 
(This method extends the list by appending elements from an iterable.)

## 3 . `Insert()`
                                              
### •	Description
List insert() method in Python is very useful to insert an element in a list. What makes it different from append() is that the list insert() function can add the value at any position in a list, whereas the append function is limited to adding values at the end.
### •	Syntax 
```
fruit : list = ["banana","cherry","grape"]
fruit.insert(1,"apple")
print(fruit)
```
### •	Return Type None 
(This method inserts an element at a specified position.)

## 4 .`Remove()`
                                              
### •	Description
List remove() function in Python removes the first occurrence of a given item from the list. It make changes to the current list. It only takes one argument that is the element you want to remove and if that element is not present in the list, it gives ValueError.
### •	Syntax 
```
lis : list = ['a', 'b', 'c']
lis.remove("b")
print(lis)
```
### •	Return Type None 
(This method removes the first occurrence of a specified value.)

## 5 .`Pop()`
                                              
### • Description
List pop() function removes and returns the value at a specific index from a list. It is an inbuilt function of Python.
It can be used with and without parameters; without a parameter list pop() returns and removes the last value from the list by default, but when given an index value as a parameter, it only returns and removes the element at that index.
### •	Syntax 
Without parameter it will remove the last element
```
fruits : list = ["apple", "mango", "cherry"]
fruits.pop()
print(fruits)
```
With parameter it will remove the desired  element
```
my_list : list = [1, 2, 3, 4, 5, 6]
poped_item = my_list.pop(-2)
print("New list", my_list)
```
### •	Return Type
Returns the element that was removed from the list. If no index is specified, It removes and returns the last item.

## 6 . `Clear()`
                                              
### •	Description
Python List clear() method removes all items from the List making it an empty/null list.
### •	Syntax 
```
my_list : list = [1, 2, 3, 4, 5, 6]
lis.clear()
print( my_list)
```
### •	Return Type
None ( This method removes all elements from the list.)

## 7 . `Index()`
                                              
### •	Description
Python list index() method is used to find position of element in list.
It returns the position of the first occurrence of that element in the list. If the item is not found in the list, index() function raises a “ValueError” error 
### •	Syntax 
```
Animals : list= ["cat", "dog", "tiger"]
print(Animals.index("dog"))

```
### •	Return Type
Returns an integer. This method returns the index of the first occurrence of a specified value.

## 8 . `Count()`
                                              
### •	Description
Python list count() function lets you count the occurrence of an element in a list. It returns the count of how many times an element is present in a list.
### •	Syntax 
```
fruits : list = ["Apple", "Mango", "Banana", "Cherry" , "Papaya"]
print(fruits.count("Apple"))
```
### •	Return Type
Returns an integer. This method returns the number of times a specified value appears in the list.


## 9 .	`Pop()`
                                              
### •	Description
Python list sort() method sorts the elements of a list. It sorts in ascending order by default but can also sort values in descending order or in a custom manner using its parameters.
###•	Syntax 
Without parameter it will sort in ascending order
```
random_numbers : list = [2,5,6,1,8,3]
random_numbers.sort ()
print(random_numbers)
```
With parameter it will sort in ascending order
```
numbers : list = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers)
```
### •	Return Type
Returns None. This method sorts the list in ascending order and in ascending order

## 10.	`Reverse()`
                                              
### •	Description
It reverses objects of the List in place i.e. it doesn’t use any extra space but it just modifies the original list
### •	Syntax 
```
list1 : list = [1, 2, 3, 4, 1, 2, 6] 
list1.reverse() 
print(list1) 
```
### •	Return Type
Returns None. This method reverses the elements of the list in place.

## 11.	`Copy()`
                                              
### •	Description
 The list Copy() method makes a new shallow copy of a list.

•	Syntax 
```
fruits : list = ["mango","apple","strawberry"]
shakes = fruits.copy()
print(shakes)
```
## •	Return Type
Returns a new list. This method returns a shallow copy of the list.












	