# # f = open("file.txt" , "r+")

# # # Read the content of the file

# # content = f.read()
# # print(content)
# # # Close the file

# # f.close()

# # w=open("file2.txt" , "w")
# # w.write("Hello , how are you ? ")
# # w.write("\nHello , how are you 2? ")
# # # Close the file

# # w.close()

# # r=open("file2.txt" , "r")

# # # Read the content of the file  

# # content = r.read()
# # print(content)

# # # Close the file
# # # r.close()
# # w  = open("file.txt" , "w")

# # # Write some content to the file

# # w.write("Hello , how are you ? ")
# # w.write("\nHello , how are you 2? ")

# # # Close the file

# # w.close()

# # r = open("file.txt" , "r")

# # # Read the content of the file

# # content = r.read()
# # print(content)

# # # Close the file

# # r.close()
# # a = open("file.txt" , "a")

# # # Write some content to the file

# # a.write("\nHello , how are you 3? ")

# # # Close the file

# # a.close()

# # r = open("file.txt" , "r")

# # # Read the content of the file

# # content = r.read()
# # content.split()

# # # Close the file

# # r.close()

# # print(content)

# # r = open("file2.txt" , "r")

# # # # Read the content of the file
# # con = r.read()
# # words = con.split()
# # # print(words)

# wb= open("binary.bin" , "wb")

# # # Write some binary data to the file
# wb.write(b'1,2')
# wb.close()
# # read
# rb = open("binary.bin" , "rb")
# # Read the content of the file

# content = rb.read()

# print(content)

# # Close the file

# rb.close()
# # Writing to a binary file
# # with open("example.bin", "wb") as file:
# #     file.write(b'Binary data to write')  # Write binary data

# # # Reading from the same binary file
# # with open("example.bin", "rb") as file:
# #     data = file.read()  # Read the content
# #     print(data)


# file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# s = "Hello\n"

# # Writing a string to file
# file1.write(s)

# # Writing multiple strings at a time
# file1.writelines(L)

# # Closing file
# file1.close()

# # Checking if the data is written to file or not
# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()

# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()

# # Append-adds at last
# file1 = open("myfile.txt", "a")  # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()

# # Write overwrites
# file1 = open("myfile.txt", "w")  # write mode
# file1.write("Tomorrow \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()44

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


# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()