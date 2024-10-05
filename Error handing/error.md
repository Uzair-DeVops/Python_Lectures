
# Errors and Exceptions in Python 

Errors in Python can be of two types: **Syntax Errors** and **Exceptions**. Errors are issues in a program that cause the program to stop execution. On the other hand, exceptions are raised when some internal events occur that change the normal flow of the program.

## Types of Exceptions in Python

In Python, there are several built-in exceptions that can be raised when an error occurs during program execution. Some of the most common types are:

- **SyntaxError**: Raised when the interpreter encounters a syntax error, such as a missing colon or unbalanced parenthesis.
- **TypeError**: Raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
- **NameError**: Raised when a variable or function name is not found in the current scope.
- **IndexError**: Raised when an index is out of range for a list, tuple, or sequence.
- **KeyError**: Raised when a key is not found in a dictionary.
- **ValueError**: Raised when a function receives an invalid argument, such as converting an invalid string to an integer.
- **AttributeError**: Raised when an attribute or method is not found on an object.
- **IOError**: Raised when an I/O operation fails, such as reading or writing to a file.
- **ZeroDivisionError**: Raised when trying to divide a number by zero.
- **ImportError**: Raised when an import statement fails to find or load a module.

## Difference between Syntax Errors and Exceptions

### Syntax Error
A syntax error occurs due to incorrect syntax in the code, causing the program to terminate.

Example:

```python
amount = 10000
if(amount > 2999)
print("You are eligible to purchase DSA Self Paced")
```

### Exceptions
Exceptions occur when the code is syntactically correct but results in an error during execution. This doesn't stop the program, but it changes its normal flow.

Example:

```python
marks = 10000
a = marks / 0
print(a)
```

This will raise a `ZeroDivisionError` because dividing by zero is not allowed.

## Handling Exceptions

### TypeError Example
A `TypeError` is raised when incompatible types are used in an operation.

```python
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")
```

### Try and Except Statement

`try` and `except` blocks are used to catch and handle exceptions in Python.

Example:

```python
a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))
    print("Fourth element = %d" % (a[3]))
except:
    print("An error occurred")
```

### Catching Specific Exceptions

You can catch specific exceptions like `IndexError` or `ValueError`.

```python
try:
    # statements
except IndexError:
    # handle IndexError
except ValueError:
    # handle ValueError
```

### Example of Specific Exception Handling

```python
def fun(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
```

## Try with Else Clause

The `else` clause executes only if the `try` block doesn't raise an exception.

Example:

```python
def AbyB(a, b):
    try:
        c = (a + b) / (a - b)
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
```

To handle a syntax error using error handling in Python, you can use a `try-except` block. However, keep in mind that a `SyntaxError` occurs at compile time, meaning the Python interpreter will not even run the code if it detects a syntax error. Therefore, you cannot catch a `SyntaxError` using `try-except` within the code that has the error itself.

However, you can catch `SyntaxError` when dynamically executing code using `eval()` or `exec()`. Here's an example of handling a `SyntaxError` in such cases:

```python
code = "print('Hello World'"  # SyntaxError: missing closing parenthesis

try:
    exec(code)  # Using exec to run the code
except SyntaxError as e:
    print(f"Syntax error occurred: {e}")
```


## Finally Keyword in Python

The `finally` block is always executed, regardless of whether an exception occurs.

```python
try:
    k = 5 // 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is always executed")
```
# finally 

### there may be some situation in which the current method ends up while handling some exceptions. But the method may require some additional steps before its termination, like closing a file or a network and so on. So, in order to handle these situations, Python provides a keyword finally, which is always executed after try and except blocks. The finally block always executes after normal termination of try block or after try block terminates due to some exception.


### Important Points –

- finally block is always executed after leaving the try statement. In case if some exception was not handled by except block, it is re-raised after execution of finally block.
- finally block is used to deallocate the system resources.
One can use finally just after try without using except block, but no exception is handled in that case.

```python
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: An error occurred while reading the file.")
finally:
    print("Closing the file.")
    if file:
        file.close()
```