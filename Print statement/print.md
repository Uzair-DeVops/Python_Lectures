# Print() Function

Python print() function prints the message to the screen or any other standard output device




# Easy explanation
The print() function in Python is used to display output on the screen. It's one of the most basic yet powerful functions, helping you see messages, values, and results of your code. You simply pass what you want to print inside the parentheses, and Python will display it.

Example 1: Printing a Simple Message  
In this example, we'll print a basic message to the screen.

```python
print("Hello, World!")
```

Output:

```
Hello, World!
```
# what is string
### Anything written inside inverted commas is called string (will explain this concept in upcoming classes)

# Commas in print functions

## single comma

```python
print('Hello, World!')
```

## double comma

```python
print("Hello, World!")
```

## triple comma

```python
print('''Hello, World!''')
```

# difference between them

### you will use single comma when you need to use double comma inside 
### you will use double comma when you need to use single comma inside
### you will use triple comma when you need to use double comma and single comma inside
### triple comma also use for writing double line string 


# Parameters in print function



## Python end parameter in print()  

By default, Python's print() function ends with a newline. A programmer with C/C++ background may wonder how to print without a newline. Python’s print() function comes with a parameter called ‘end‘. By default, the value of this parameter is ‘\n’, i.e., the new line character.  

Example 1:  
Here, we can end a print statement with any character/string using this parameter.  

```python
# ends the output with a space
print("Welcome to", end = ' ')
print("GeeksforGeeks", end= ' ')
```


# Easy Explanation


The `end` parameter in the `print()` function lets you control what appears at the end of the printed output. By default, `print()` adds a newline (`\n`) at the end, so each `print()` call starts on a new line. With `end`, you can change this to any other character or string, like a space or comma, or even prevent a new line entirely.

### Example 1: Using `end` to Print on the Same Line

Here, we'll print multiple items on the same line by changing the `end` parameter.

```python
print("Hello", end=" ")
print("World!")
```

**Output:**
```
Hello World!
```

In this example, `end=" "` adds a space instead of a new line, so the next `print()` statement continues on the same line.

### Example 2: Using `end` with Custom Text

You can also set `end` to any string. Here, we’ll use `end=" - "` to separate items.

```python
print("Python", end=" - ")
print("is", end=" - ")
print("fun!")
```

**Output:**
```
Python - is - fun!
```

In this case, each `print()` adds `" - "` at the end, creating a custom separator. This is useful when you want to format your output in a specific way.



# Easy and more explanation


### sep parameter in print()  

The separator between the arguments to print() function in Python is space by default (softspace feature), which can be modified and can be made to any character, integer, or string as per our choice. The ‘sep’ parameter is used to achieve the same, and it is found only in Python 3.x or later. It is also used for formatting the output strings.  

Examples:

```python
# code for disabling the softspace feature 
print('G','F','G', sep='') 

# for formatting a date 
print('09','12','2016', sep='-') 

# another example 
print('pratik','geeksforgeeks', sep='@')


```

The `sep` parameter in the `print()` function controls how multiple items are separated when printed. By default, `sep` is set to a single space (`' '`), so when you provide multiple arguments to `print()`, they are separated by a space.

### Usage of `sep`

If you want to use a different separator, you can specify it using the `sep` parameter. This can be any string, such as a comma, hyphen, newline, or even an empty string.

### Syntax
```python
print(object1, object2, ..., sep='separator')
```

### Examples

#### 1. Default `sep` (space)
When you don’t specify `sep`, `print()` separates each argument with a space.
```python
print("apple", "banana", "cherry")  # Output: apple banana cherry
```

#### 2. Custom Separator: Comma
Using `sep=","` places a comma between each item.
```python
print("apple", "banana", "cherry", sep=", ")  # Output: apple, banana, cherry
```

#### 3. Custom Separator: Hyphen
Using `sep="-"` places a hyphen between each item.
```python
print("apple", "banana", "cherry", sep="-")  # Output: apple-banana-cherry
```

#### 4. Custom Separator: Empty String
Using `sep=""` places no space between items, concatenating them directly.
```python
print("apple", "banana", "cherry", sep="")  # Output: applebananacherry
```

#### 5. Custom Separator: Newline
Using `sep="\n"` places each item on a new line.
```python
print("apple", "banana", "cherry", sep="\n")
# Output:
# apple
# banana
# cherry
```

### Why Use `sep`?

The `sep` parameter is handy when formatting output without needing to manually concatenate strings. It can make the code cleaner and easier to read, especially when dealing with a large number of items or dynamic data.


# summary table

| Parameter | Default | Description                           | Example Usage                          | Example Output                  |
|-----------|---------|---------------------------------------|----------------------------------------|---------------------------------|
| `sep`     | `' '`   | Specifies the separator between multiple objects | `print("apple", "banana", sep=", ")`  | `apple, banana`                 |
| `end`     | `'\n'`  | Specifies the string appended at the end of the output | `print("Hello", end="!")`             | `Hello!` (no newline after)



# An escape sequence
 In Python is a special way to represent certain characters in a string that are otherwise hard to include. They start with a backslash (`\`) and tell Python to interpret the next character in a specific way. For example, `\n` is an escape sequence for a new line, so when Python sees it, it moves to the next line in the output.

### Example 1: New Line (`\n`)
The `\n` escape sequence creates a new line in a string.

```python
text = "Hello,\nWorld!"
print(text)
```

**Output:**
```
Hello,
World!
```

Here, `\n` tells Python to break the line, so "World!" appears on a new line.

### Example 2: Tab (`\t`)
The `\t` escape sequence adds a horizontal tab space in a string.

```python
text = "Hello,\tWorld!"
print(text)
```

**Output:**
```
Hello,   World!
```

In this example, `\t` adds a tab space between "Hello," and "World!". Escape sequences make it easier to control formatting in strings.


# More information

Escape sequences in Python's `print()` function allow you to include special characters within strings. These sequences start with a backslash (`\`) followed by a character, letting you insert things like newlines, tabs, quotes, or even Unicode characters.

### Common Escape Sequences

| Escape Sequence | Description                 | Example Usage               | Output                          |
|-----------------|-----------------------------|-----------------------------|---------------------------------|
| `\n`            | Newline                     | `print("Hello\nWorld")`     | `Hello`<br>`World`              |
| `\t`            | Horizontal Tab              | `print("Hello\tWorld")`     | `Hello    World`                |
| `\\`            | Backslash                   | `print("This is a backslash: \\")` | `This is a backslash: \`       |
| `\'`            | Single Quote                | `print('It\'s Python')`     | `It's Python`                   |
| `\"`            | Double Quote                | `print("He said, \"Hi\"")`  | `He said, "Hi"`                 |
| `\r`            | Carriage Return             | `print("Hello\rWorld")`     | `World` (overwrites "Hello")    |
| `\b`            | Backspace                   | `print("Hello\bWorld")`     | `HellWorld` (removes "o")       |
| `\f`            | Form Feed                   | `print("Hello\fWorld")`     | `Hello`<br>`      World`        |
| `\uXXXX`        | Unicode Character (16-bit)  | `print("\u2764")`           | ❤️ (heart symbol)               |
| `\UXXXXXXXX`    | Unicode Character (32-bit)  | `print("\U0001F600")`       | 😀 (grinning face emoji)        |
| `\xXX`          | ASCII Character (hex)       | `print("\x48\x69")`         | `Hi`                            |
| `\N{name}`      | Named Unicode Character     | `print("\N{check mark}")`   | ✅                              |

### Examples

1. **Newline (`\n`)**
   ```python
   print("Hello\nWorld")
   # Output:
   # Hello
   # World
   ```

2. **Tab (`\t`)**
   ```python
   print("Hello\tWorld")
   # Output: Hello    World
   ```

3. **Unicode Character (`\u` and `\U`)**
   ```python
   print("\u2764")  # Output: ❤️ (heart symbol)
   print("\U0001F600")  # Output: 😀 (grinning face emoji)
   ```

4. **Double Quote (`\"`) and Single Quote (`\'`)**
   ```python
   print("She said, \"Hi\"")
   # Output: She said, "Hi"
   
   print('It\'s Python')
   # Output: It's Python
   ```

5. **Backslash (`\\`)**
   ```python
   print("This is a backslash: \\")
   # Output: This is a backslash: \
   ```

Escape sequences are a powerful tool in `print()` for handling special characters and formatting strings precisely.