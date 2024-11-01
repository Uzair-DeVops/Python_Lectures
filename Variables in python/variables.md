# Variables 
Python Variable is containers that store values. Python is not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it.
In Python, variables are used to store data values that can be accessed and manipulated throughout a program. Python variables don’t require explicit declaration of types, as Python is dynamically typed, meaning it automatically determines the variable’s type based on the assigned value.

### Declaring Variables
In Python, you can create a variable simply by assigning a value to a name:

```python
x = 10          # integer
name = "Alice"  # string
pi = 3.14       # float
is_active = True  # boolean
```

### Rules for Naming Variables

1. **Start with a letter or underscore**: Variable names must begin with a letter (a-z, A-Z) or an underscore (_).
2. **Can contain letters, numbers, and underscores**: After the first character, variables can have letters, numbers, and underscores.
3. **Case-sensitive**: `name` and `Name` are treated as two different variables.
4. **Avoid reserved words**: You cannot use Python keywords (like `if`, `for`, `while`, etc.) as variable names.

### Examples of Valid Variable Names

```python
age = 25
first_name = "John"
_is_active = True
score_1 = 95
```

### Examples of Invalid Variable Names

```python
1st_place = "Gold"    # Starts with a number
first-name = "John"   # Contains a hyphen
for = 10              # Uses a reserved keyword
```

### Assigning Multiple Variables at Once

You can assign values to multiple variables in a single line:

```python
x, y, z = 1, 2, 3
```

Or, assign the same value to multiple variables:

```python
a = b = c = 5
```

### Data Types in Variables

Python variables can store different types of data. Here are the most common data types:

1. **Integers (`int`)**: Whole numbers, like `10`, `-3`, or `1000`.
2. **Floats (`float`)**: Decimal numbers, like `3.14` or `0.001`.
3. **Strings (`str`)**: Text enclosed in quotes, like `"Hello"` or `'World'`.
4. **Booleans (`bool`)**: Logical values `True` or `False`.
5. **Lists (`list`)**: Ordered collections of items, like `[1, 2, 3]`.
6. **Dictionaries (`dict`)**: Key-value pairs, like `{"name": "Alice", "age": 25}`.
7. **Tuples (`tuple`)**: Ordered, immutable collections, like `(1, 2, 3)`.
8. **Sets (`set`)**: Unordered collections of unique items, like `{1, 2, 3}`.

### Example Usage

```python
name = "John"
age = 30
height = 5.9
is_student = True

print(name, "is", age, "years old and", height, "feet tall.")
# Output: John is 30 years old and 5.9 feet tall.
```

### Variable Type Conversion

You can convert variable types using functions like `int()`, `float()`, `str()`, etc.

```python
x = "10"
y = int(x)  # y is now an integer with value 10

pi = 3.14
str_pi = str(pi)  # str_pi is now a string with value "3.14"
```

### Updating Variable Values

You can update a variable by reassigning it:

```python
count = 10
count = count + 5  # Now count is 15
```

Or, use shorthand operators:

```python
count += 5  # Equivalent to count = count + 5
```

### Variable Scope

1. **Local Variables**: Defined inside functions and accessible only within that function.
2. **Global Variables**: Defined outside functions and accessible anywhere in the code.

Example of a global and local variable:

```python
x = "global"

def my_function():
    x = "local"
    print(x)  # Output: local

my_function()
print(x)  # Output: global
```

### Summary
- Variables store data and don’t require explicit types.
- Follow naming conventions and avoid using reserved keywords.
- Variables can store various data types, which can be converted as needed.
- Use global and local scopes carefully to manage variable access and avoid conflicts.