
# Python Lists

a list is a collection of things, enclosed in `[]` and separated by commas.

The list is a sequence data type which is used to store the collection of data. Tuples and Strings are other types of sequence data types.

## Example of the list in Python

Here we are creating a Python List using `[]`.

```python
Var = ["Geeks", "for", "Geeks"]
print(Var)
```


## Table of Content
- Creating a List in Python
- Creating a list with multiple distinct or duplicate elements
- Getting the size of Python list
- Accessing elements from the List
- Negative indexing
- Taking Input of a Python List
- Adding Elements to a Python List
  - Using `append()` method
  - Using `insert()` method
  - Using `extend()` method
- Reversing a List in Python
  - A list can be reversed by using the `reverse()` method in Python.
  - Using the `reversed()` function:
- Removing Elements from the List
  - Using `remove()` method
  - Using `pop()` method
- Slicing of a List
- Negative index List slicing
- List Comprehension
- Basic Example on Python List
- List Methods
- Built-in functions with List

## Creating a List in Python
Lists in Python can be created by just placing the sequence inside the square brackets `[]`. Unlike Sets, a list doesn’t need a built-in function for its creation.

**Note:** Unlike Sets, the list may contain mutable elements.

### Example 1: Creating a list in Python

```python
# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])
```



### Example 2: Creating a list with multiple distinct or duplicate elements
A list may contain duplicate values with their distinct positions and hence, multiple distinct or duplicate values can be passed as a sequence at the time of list creation.

```python
# Creating a List with the use of Numbers (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with mixed datatype values (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)
```

**Output**
```plaintext
List with the use of Numbers: 
[1, 2, 4, 4, 3, 3, 3, 6, 5]

List with the use of Mixed Values: 
[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
```

## Getting the size of Python list
Python `len()` is used to get the length of the list.

```python
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))
```

**Output**
```plaintext
0
3
```

## Accessing elements from the List
In order to access the list items, refer to the index number. Use the index operator `[]` to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing.

### Example 1: Accessing elements from list
```python
# Creating a List with the use of multiple values
List = ["Geeks", "For", "Geeks"]

# accessing an element from the list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
```

**Output**
```plaintext
Accessing a element from the list
Geeks
Geeks
```

### Example 2: Accessing elements from a multi-dimensional list
```python
# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the Multi-Dimensional List using index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
```

**Output**
```plaintext
Accessing a element from a Multi-Dimensional list
For
Geeks
```

## Negative indexing
In Python, negative sequence indexes represent positions from the end of the List. Instead of having to compute the offset as in `List[len(List)-3]`, it is enough to just write `List[-3]`. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

```python
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])
```

**Output**
```plaintext
Accessing element using negative indexing
Geeks
For
```

## Taking Input of a Python List
We can take the input of a list of elements as strings, integers, floats, etc. But the default one is a string.

### Example 1:
```python
# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()  
print('The list is:', lst)   # printing the list
```



<!-- ### Example 2: -->
<!-- ```python
# input size of the list
n = int(input("Enter the size of list : "))

# store integers in a list using map, split and strip functions
lst = list(map(int, input("Enter the integer elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst)
```

**Output:**
```plaintext
Enter the size of list : 4
Enter the integer elements: 6 3 9 10
The list is: [6, 3, 9, 10]
``` -->

## Adding Elements to a Python List
### Method 1: Using `append()` method
Elements can be added to the List by using the built-in `append()` function. Only one element at a time can be added to the list by using the `append()` method; for the addition of multiple elements with the `append()` method, loops are used. Tuples can also be added to the list with the use of the `append()` method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of the `append()` method.

```python
# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
```

**Output**
```plaintext
Initial blank List: 
[]

List after Addition of Three elements: 
[1, 2, 4]

List after Addition of elements from 1-3: 
[1, 2, 4, 1, 2, 3]

List after Addition of a Tuple: 
[1, 2, 4, 1, 2, 3, (5, 6)]

List after Addition of a List: 
[1, 2, 4, 1, 2

, 3, (5, 6), ['For', 'Geeks']]
```

### Method 2: Using `insert()` method
In order to insert an element at a given position in a List, we can use the `insert()` method. This method requires two parameters, `index` and `element`, and it allows you to insert the element at the specified index.

```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Adding element at 1st Position
List.insert(1, 'CODE')
print("\nList after Insertion of CODE at Position 1: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

List after Insertion of CODE at Position 1: 
['GEEKS', 'CODE', 'FOR', 'GEEKS']
```

### Method 3: Using `extend()` method
The `extend()` method is used to add multiple values to the list at once. The `extend()` method takes an iterable as an argument and adds its elements to the list.

```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Adding element at 1st Position
List.extend(['CODE', 'IN', 'PYTHON'])
print("\nList after Insertion of CODE at Position 1: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

List after Insertion of CODE at Position 1: 
['GEEKS', 'FOR', 'GEEKS', 'CODE', 'IN', 'PYTHON']
```

## Reversing a List in Python
A list can be reversed by using the `reverse()` method in Python. The reverse() method reverses the order of elements in a list in place.

### Example 1: Using `reverse()` method
```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Reversing a List
List.reverse()
print("\nReversed List: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

Reversed List: 
['GEEKS', 'FOR', 'GEEKS']
```

### Example 2: Using `reversed()` function:
```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Using `reversed()` function
reversed_List = list(reversed(List))
print("\nReversed List: ")
print(reversed_List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

Reversed List: 
['GEEKS', 'FOR', 'GEEKS']
```

## Removing Elements from the List
### Method 1: Using `remove()` method
To remove an element from a list in Python, we can use the `remove()` method. It removes the first matching value (not a specific index) from the list.

```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Removing the element 'FOR' from List
List.remove('FOR')
print("\nList after Removing FOR: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

List after Removing FOR: 
['GEEKS', 'GEEKS']
```

### Method 2: Using `pop()` method
The `pop()` method removes an element from the list at the specified position. If no position is specified, it removes and returns the last item in the list.

```python
# Creating a List
List = ['GEEKS', 'FOR', 'GEEKS']
print("Initial List: ")
print(List)

# Removing the element at index 0
List.pop(0)
print("\nList after Popping the First Element: ")
print(List)

# Removing the last element
List.pop()
print("\nList after Popping the Last Element: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['GEEKS', 'FOR', 'GEEKS']

List after Popping the First Element: 
['FOR', 'GEEKS']

List after Popping the Last Element: 
['FOR']
```

## Slicing of a List
Slicing can be done by using a colon (`:`) operator. List slicing is the method to access the elements of the list using a specific range or by specifying indexes. The syntax for slicing is as follows:

```python
list_name[start:stop:step]
```

- `start`: The index from which you want to start slicing (inclusive).
- `stop`: The index at which you want to end slicing (exclusive).
- `step`: The number of elements to skip (optional).

### Example:
```python
# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing a List
print(List[0:4])  # Output: [1, 2, 3, 4]
print(List[1:6])  # Output: [2, 3, 4, 5, 6]
print(List[3:8])  # Output: [4, 5, 6, 7, 8]
print(List[:])    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Output**
```plaintext
[1, 2, 3, 4]
[2, 3, 4, 5, 6]
[4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Negative index List slicing
In Python, you can also slice lists using negative indexes. The negative index indicates how far from the end of the list you want to slice.

### Example:
```python
# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative index slicing
print(List[-8:-4])  # Output: [2, 3, 4, 5]
print(List[-5:-1])  # Output: [5, 6, 7, 8]
```

**Output**
```plaintext
[2, 3, 4, 5]
[5, 6, 7, 8]
```

## List Comprehension
List comprehension is a way of creating lists based on existing lists. It is more concise and faster than traditional for loops.

### Example:
```python
# Traditional way
List = []
for i in range(10):
    List.append(i * 2)
print(List)

# Using List Comprehension
List = [i * 2 for i in range(10)]
print(List)
```

**Output**
```plaintext
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Basic Example on Python List
```python
# Creating a List
List = ['Geeks', 'For', 'Geeks']
print("Initial List: ")
print(List)

# Modifying a List
List[1] = "Geeks"
print("\nModified List: ")
print(List)
```

**Output**
```plaintext
Initial List: 
['Geeks', 'For', 'Geeks']

Modified List: 
['Geeks', 'Geeks', 'Geeks']
```

## List Methods
Python provides a number of built-in methods that can be used with lists. Some of the commonly used methods include:

- `append()`: Adds an element to the end of the list.
- `insert()`: Inserts an element at a specific position.
- `remove()`: Removes a specified element.
- `pop()`: Removes an element at a specified position.
- `reverse()`: Reverses the order of the elements.
- `sort()`: Sorts the elements of the list.

## Built-in functions with List
Several built-in functions can be used with lists. Some of the commonly used functions include:

- `len()`: Returns the number of elements in the list.
- `min()`: Returns the smallest element.
- `max()`: Returns the largest element.
- `sum()`: Returns the sum of the elements.
```

