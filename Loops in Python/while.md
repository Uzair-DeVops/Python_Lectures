# Python While Loop
### Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

<img src="while sytax.png">

```python
# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
```

## Infinite while Loop in Python

```python
age = 28

# the test condition is always True
while age > 19:
    print('Infinite Loop')
```

## Control Statements in Python with Examples

```python
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print('Current Letter :', a[i])
    i += 1
```

## Python while loop with a break statement
```python
# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
        
    print('Current Letter :', a[i])
    i += 1
```

## Python while loop with a pass statement

```python
# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)
```
