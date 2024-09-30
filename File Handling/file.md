

## Python File Handling
Python supports file handling and allows users to handle files, i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy. Like other concepts of Python, this concept here is also easy and short.

Python treats files differently as text or binary, and this is important. Each line of code includes a sequence of characters, and they form a text file.
 <!-- Each line of a file is terminated with a special character, called the EOL or End of Line characters like a comma `{,}` or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with reading and writing files. --> -->

<!-- ## Advantages of File Handling in Python
- **Versatility**: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
- **Flexibility**: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.) and to perform different operations on files (e.g. read, write, append, etc.).
- **User-friendly**: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
- **Cross-platform**: Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.

## Disadvantages of File Handling in Python
- **Error-prone**: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
- **Security risks**: File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
- **Complexity**: File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
- **Performance**: File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations. -->


## Python File Open
Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function `open()`, but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

```python
f = open(filename, mode)
```

Where the following mode is supported:

- `r`: open an existing file for a read operation.
- `w`: open an existing file for a write operation. If the file already contains some data, then it will be overridden, but if the file is not present then it creates the file as well.
- `a`: open an existing file for append operation. It won’t override existing data.
- `r+`: To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
- `w+`: To write and read data. It overwrites the previous file if one exists, it will truncate the file to zero length or create a file if it does not exist.
- `a+`: To append and read data from the file. It won’t override existing data.

## Working in Read Mode
There is more than one way to read from a file in Python. Let us see how we can read the content of a file in read mode.

### Example 1:
The open command will open the Python file in the read mode and the for loop will print each line present in the file.

```python
# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print(each)
```

**Output:**
```
Hello world
GeeksforGeeks
123 456
```

### Example 2:
In this example, we will extract a string that contains all characters in the Python file then we can use `file.read()`.

```python
# Python code to illustrate read() mode
file = open("geeks.txt", "r") 
print(file.read())
```

**Output:**
```
Hello world
GeeksforGeeks
123 456
```

### Example 3:
In this example, we will see how we can read a file using the `with` statement in Python.

```python
# Python code to illustrate with()
with open("geeks.txt") as file:  
    data = file.read() 

print(data)
```

**Output:**
```
Hello world
GeeksforGeeks
123 456
```

### Example 4:
Another way to read a file is to call a certain number of characters like in the following code, the interpreter will read the first five characters of stored data and return it as a string:

```python
# Python code to illustrate read() mode character wise
file = open("geeks.txt", "r")
print(file.read(5))
```

**Output:**
```
Hello
```

### Example 5:
We can also split lines while reading files in Python. The `split()` function splits the variable when space is encountered. You can also split using any characters as you wish.

```python
# Python code to illustrate split() function
with open("geeks.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
```

**Output:**
```
['Hello', 'world']
['GeeksforGeeks']
['123', '456']
```



# Reading from a File

There are three ways to read data from a text file:

- **`read()`**: Returns the read bytes in the form of a string. Reads `n` bytes; if no `n` is specified, reads the entire file.
  
  ```python
  File_object.read([n])
  ```

- **`readline()`**: Reads a line of the file and returns it in the form of a string. For a specified `n`, reads at most `n` bytes. However, it does not read more than one line, even if `n` exceeds the length of the line.
  
  ```python
  File_object.readline([n])
  ```

- **`readlines()`**: Reads all the lines and returns them as each line in a string element in a list.
  
  ```python
  File_object.readlines()
  ```

**Note**: `'\n'` is treated as a special character of two bytes.

## Example

```python
# Program to show various ways to read data from a file.

# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show the difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
```

**Output**:

```
Output of Read function is
Hello
This is Delhi
This is Paris
This is London

Output of Readline function is
Hello

Output of Read(9) function is
Hello
Th

Output of Readline(9) function is
Hello

Output of Readlines function is
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']
```

## Using the `with` Statement

The `with` statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call `file.close()` when using the `with` statement. The `with` statement itself ensures proper acquisition and release of resources.

### Syntax

```python
with open(filename) as file:
```

### Example

```python
# Program to show various ways to read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())
```

**Output**:

```
Hello
This is Delhi
This is Paris
This is London
```







## Creating a File using the `write()` Function
Just like reading a file in Python, there are a number of ways to write to a file in Python. Let us see how we can write the content of a file using the `write()` function in Python.



## Working in Write Mode
Let’s see how to create a file and how the write mode works.

### Example 1:
In this example, we will see how the write mode and the `write()` function are used to write in a file. The `close()` command terminates all the resources in use and frees the system of this particular program.

```python
# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
```

**Output:**
```
This is the write commandIt allows us to write in a particular file
```

### Example 2:
We can also use the written statement along with the `with()` function.

```python
# Python code to illustrate with() along with write()
with open("file.txt", "w") as f: 
    f.write("Hello World!!!") 
```

**Output:**
```
Hello World!!!
```





# Writing to File

There are two ways to write to a file:

- **`write()`**: Inserts the string `str1` in a single line in the text file.
  
  ```python
  File_object.write(str1)
  ```

- **`writelines()`**: For a list of string elements, each string is inserted in the text file. This is used to insert multiple strings at a single time.
  
  ```python
  File_object.writelines(L)  # for L = [str1, str2, str3]
  ```

**Note**: `'\n'` is treated as a special character of two bytes.

## Example

```python
# Python program to demonstrate writing to a file

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()
```

**Output**:

```
Hello
This is Delhi
This is Paris
This is London
```




# Appending Data to a File

In order to append a new line to the existing file, open the file in append mode by using either `'a'` or `'a+'` as the access mode. The definitions of these access modes are as follows:

- **Append Only (`'a'`)**: Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

- **Append and Read (`'a+'`)**: Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

When the file is opened in append mode, the handle is positioned at the end of the file, and the data being written will be inserted at the end, after the existing data. Let’s see the example below to clarify the difference between write mode and append mode.

## Example

```python
# Python program to illustrate Append vs Write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
```

**Output**:

```
Output of Readlines after appending
This is Delhi
This is Paris
This is LondonToday

Output of Readlines after writing
Tomorrow
```

## Append Data from New Line

In the above example, it can be seen that the data is not appended from a new line. This can be done by writing the newline `'\n'` character to the file.

**Note**: `'\n'` is treated as a special character of two bytes.

## Example

```python
# Python program to illustrate append from new line
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append adds at last
# append mode
file1 = open("myfile.txt", "a")

# writing newline character
file1.write("\n")
file1.write("Today")

# without newline character
file1.write("Tomorrow")

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
```

**Output**:

```
Output of Readlines after appending
This is Delhi
This is Paris
This is London
TodayTomorrow
```

## Using the With Statement

The `with` statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call `file.close()` when using the `with` statement. The `with` statement itself ensures proper acquisition and release of resources.

## Example

```python
# Program to show various ways to append data to a file using the with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

# Appending to file
with open("myfile.txt", 'a') as file1:
    file1.write("Today")

# Reading from file
with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())
```

**Output**:

```
Hello
This is Delhi
This is Paris
This is London
Today
```











## Appending to a File

When the file is opened in append mode, the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data. Let’s see the example below to clarify the difference between write mode and append mode.

```python
# Python program to illustrate Append vs Write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

# Append adds at the end
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
```

**Output**:

```
Output of Readlines after appending
This is Delhi
This is Paris
This is London
Today

Output of Readlines after writing
Tomorrow
```



















## Working of Append Mode
Let us see how the append mode works.

### Example:
For this example, we will use the Python file created in the previous example.

```python
# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()
```
















## Types of Files

### Text Files
In this type of file, each line of text is terminated with a special character called EOL (End of Line), which is the new line character (`'\n'`) in Python by default.

### Binary Files
In this type of file, there is no terminator for a line, and the data is stored after converting it into machine-understandable binary language.

## Opening a File
Opening a file refers to getting the file ready either for reading or for writing. This can be done using the `open()` function. This function returns a file object and takes two arguments: one that accepts the file name and another that accepts the mode (Access Mode). 

Now, the question arises: what is the access mode? Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s opened. These modes also define the location of the File Handle in the file. The File Handle is like a cursor, which defines from where the data has to be read or written in the file.

There are 6 access modes in Python:

- **Read Only (`'r'`)**: Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exist, raises an I/O error. This is also the default mode in which the file is opened.
  
- **Read and Write (`'r+'`)**: Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
  
- **Write Only (`'w'`)**: Open the file for writing. For existing files, the data is truncated and overwritten. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
  
- **Write and Read (`'w+'`)**: Open the file for reading and writing. For existing files, data is truncated and overwritten. The handle is positioned at the beginning of the file.
  
- **Append Only (`'a'`)**: Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
  
- **Append and Read (`'a+'`)**: Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

### Binary Modes
- **Read Only in Binary format (`'rb'`)**: Opens the file for reading in binary format.
  
- **Read and Write in Binary Format (`'rb+'`)**: Opens the file for reading and writing in binary format.
  
- **Write Only in Binary Format (`'c'`)**: Opens the file for writing in binary format. If the file does not exist, a new file gets created. The content will get overwritten if the file exists.
  
- **Write and Read in Binary Format (`'wb+'`)**: Opens the file for reading and writing in binary format. A new file gets created if the file does not exist. The content will get overwritten if the file exists.
  
- **Append only in Binary Format (`'ab'`)**: Opens the file for appending in binary format. A new file gets created if there is no file. The data will be inserted at the end if the file exists.
  
- **Append and Read in Binary Format (`'ab+'`)**: Opens the file for appending and reading in binary format. A new file will be created if it does not exist.

## Syntax
```python
File_object = open("File_Name", "Access_Mode")
```

**Note**: The file should exist in the same directory as the Python script; otherwise, the full address of the file should be written.


Here are examples for each of the binary file modes in Python:

### 1. Read Only in Binary Format (`'rb'`)

This mode is used to read data from a binary file.

```python
# Example: Reading from a binary file
with open("example.bin", "rb") as file:
    data = file.read()  # Read the entire content
    print(data)
```

### 2. Read and Write in Binary Format (`'rb+'`)

This mode allows both reading and writing to a binary file.

```python
# Example: Reading and writing to a binary file
with open("example.bin", "rb+") as file:
    data = file.read()  # Read the entire content
    print(data)
    file.seek(0)  # Move the cursor to the start of the file
    file.write(b'New binary data')  # Write new data (binary)
```

### 3. Write Only in Binary Format (`'wb'`)

This mode is used to write data to a binary file. If the file exists, it will be overwritten.

```python
# Example: Writing to a binary file
with open("example.bin", "wb") as file:
    file.write(b'Binary data to write')  # Write data (binary)
```

### 4. Write and Read in Binary Format (`'wb+'`)

This mode allows writing to a binary file and reading from it. If the file exists, it will be overwritten.

```python
# Example: Writing and reading from a binary file
with open("example.bin", "wb+") as file:
    file.write(b'Binary data to write')  # Write data
    file.seek(0)  # Move the cursor to the start of the file
    data = file.read()  # Read the content
    print(data)
```

### 5. Append Only in Binary Format (`'ab'`)

This mode is used to append data to the end of a binary file. If the file does not exist, it creates a new one.

```python
# Example: Appending to a binary file
with open("example.bin", "ab") as file:
    file.write(b'Appending new binary data')  # Append data
```

### 6. Append and Read in Binary Format (`'ab+'`)

This mode allows both appending to and reading from a binary file. If the file does not exist, it creates a new one.

```python
# Example: Appending and reading from a binary file
with open("example.bin", "ab+") as file:
    file.write(b'Appending more binary data')  # Append data
    file.seek(0)  # Move the cursor to the start of the file
    data = file.read()  # Read the content
    print(data)
```

### Summary
- Use **`'rb'`** to read binary files.
- Use **`'rb+'`** to read and write without truncating the file.
- Use **`'wb'`** to write and overwrite a binary file.
- Use **`'wb+'`** to write and read from a binary file.
- Use **`'ab'`** to append data to a binary file.
- Use **`'ab+'`** to append and read from a binary file. 

These examples demonstrate basic operations for handling binary files in Python. Adjust the file names and data as needed for your use case!