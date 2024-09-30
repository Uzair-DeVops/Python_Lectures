# Python If Else Statements – Conditional Statements

### In both real life and programming, decision-making is crucial. We often face situations where we need to make choices, and based on those choices, we determine our next actions. Similarly, in programming, we encounter scenarios where we must make decisions to control the flow of our code.
### As the name suggests, If-Else statements offer two paths, allowing for different outcomes depending on the condition evaluated.


## Types of Control Flow in Python

<ol>
  <li>Python If Statement</li>
  <li>Python If Else Statement</li>
  <li>Python Elif</li>
  <li>Python Nested If Statement</li>
  <li>Ternary Statement | Short Hand If Else Statement</li>
</ol>

## Python If Statement
### The if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not.
<img src="if statement flow.png" width = "300px" style="margin-left : 400px;"> 

## Syntax

<img src="syantax of if statement.png" >

# Example of Python if Statement

```Python
i = 10

if (i > 15):
    print("10 is less than 15")
print("I am Not in if")
```

# Python If Else Statement
### The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with the if statement Python to execute a block of code when the Python if condition is false. 

## Flowchart of If Else Statement

<img src="if else statement flow.png" width = "300px" style="margin-left : 400px;"> 

## Syntax of If Else in Python
<img src="syantax of if else statement.png" >


## Example of Python If Else Statement

```Python
i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

```
## Python Elif

### Here, a user can decide among multiple options. The if statements are executed from the top down.

### As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final “else” statement will be executed.

## Flowchart of Elif Statement in Python
<img src="if elif statement flow.png" width = "700px" style="margin-left : 200px;"> 

## Syntax of If Elif in Python
<img src="syantax of if elif statement.png" >

## Example of Python If Elif Statement

```Python

i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")
```
## Python Nested If Statement
###  Nested if statements mean an if statement inside another if statement.

## Flowchart of Nested If Statement in Python
<img src="Nested if statement flow.png" width = "700px" style="margin-left : 200px;"> 

## Syntax of Nested If in Python
<img src="syantax of if nested if statement.png" >

## Example of Python Nested If Statement

```Python
i = 10
if (i == 10):
  
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
```

## Ternary Statement | Short Hand If Else Statement
### Whenever there is only a single statement to be executed inside the if block then shorthand if can be used. The statement can be put on the same line as the if statement. 

## Syntax of Ternary or Short hand If Else in Python
<img src="syantax of short hand.png" >

## Example of Python Shorthand If Statement
```Python
i = 10
if i < 15: print("i is less than 15")
```
## Example of Python Shorthand If Else Statement
```Python 
i = 10
print(True) if i < 15 else print(False)
```
