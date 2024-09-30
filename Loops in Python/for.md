# For Loops in Python

### Python For loop is used for iterating over an iterable like a String, Tuple, List, Set, or Dictionary. 

## Table of Content

1. How to use the for loop in Python
1. Python For Loop Syntax
1. Python For Loop with String
1. Python for loop with Range
1. Python for loop Enumerate
1. Nested For Loops in Python
1. Python For Loop Over List
1. Control Statements that can be used with For Loop in Python


## How to use the for loop in Python
### In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) or any iterable object. The basic syntax of the for loop is:
## Python For Loop Syntax
<img src="syantax of for loop.png">

## Python For Loop with String
```python
# Iterating over a String
print("String Iteration")

s = "Geeks"
for i in s:
    print(i)
```

## Python for loop with Range
```python
for i in range(0, 10, 2):
    print(i)
```
## Python for loop Enumerate
### In Python, the enumerate() function is used with the for loop to iterate over an iterable while also keeping track of the index of each item.
```python
l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)
```
## Nested For Loops in Python
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```
## Python For Loop Over List
``` python
# Python program to illustrate
# Iterating over a list
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)
```
## Continue in Python For Loop
### Python Continue Statement skips the execution of the program block after the continue statement and forces the control to start the next iteration.
``` python

for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)
```

## Printing range with Python Continue Statement
``` python
# loop from 1 to 10
for i in range(1, 11):

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")
```

## Break in Python For Loop
### Python break is used to terminate the execution of the loop. 
```python
for i in range(10):
    print(i)
    if i == 2:
        break
```
## Example 2: 

```python
# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop"    )
print()

i = 0

```

## For Loop in Python with Pass Statement
### When the user does not know what code to write, So user simply places a pass at that line. Sometimes, the pass is used when the user doesn’t want any code to execute. So users can simply place a pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. So using a pass statement user avoids this error

```python
n = 26

if n > 26:
	# write code your here

print('Geeks')
```
## Example 2
```python
li =['a', 'b', 'c', 'd']

for i in li:
	if(i =='a'):
		pass
	else:
		print(i)
```
## For Loops in Python with Else Statement
### The else block in a for loop is used to execute a block of code when the loop finishes
### The else block is executed only when the loop doesn’t encounter a break statement

```python
# Python program to demonstrate
# for-else loop

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
```


