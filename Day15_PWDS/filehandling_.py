# File Handling in Python:

# File handling is a crucial aspect of programming that allows you to read from and write to files on your computer. 
# In Python, you can use built-in functions to work with files.
# Here's a basic overview of how to handle files in Python:


# 1. Opening a File:
# You can open a file using the built-in open() function. 
# The open() function takes two arguments: the file name (or path) and the mode in which you want to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending). 
# Example while opening a file:
"""
file = open('example.txt', 'r')  # Open the file in read mode
content = file.read()  # Read the contents of the file    
file.close()  # Close the file after you're done

with open('example.txt', 'r') as file:  # Open the file using a context manager
    content = file.read()  # Read the contents of the file
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised. 


"""

# 2. Reading from a File:
# You can read the contents of a file using methods like read(), readline(), or readlines().
# - read(): Reads the entire contents of the file as a single string.
# - readline(): Reads a single line from the file.  
# - readlines(): Reads all the lines in the file and returns them as a list of strings.
# Example while reading a file:
"""
with open('example.txt', 'r') as file:  # Open the file in read mode
    content = file.read()  # Read the entire contents of the file
    print(content)  # Print the contents of the file

with open('example.txt', 'r') as file:  # Open the file in read mode
    line = file.readline()  # Read the first line of the file
    print(line)  # Print the first line of the file

with open('example.txt', 'r') as file:  # Open the file in read mode
    lines = file.readlines()  # Read all lines of the file into a list
    print(lines)  # Print the list of lines from the file
"""

# 3. Writing to a File:     
# You can write to a file using methods like write() or writelines().
# - write(): Writes a string to the file.
# - writelines(): Writes a list of strings to the file.
# Example while writing to a file:
"""
with open('example.txt', 'w') as file:  # Open the file in write mode
    file.write("Hello, World!\n")  # Write a string to the file
    file.write("Welcome to file handling in Python.\n")  # Write another string to the file
    

with open('example.txt', 'w') as file:  # Open the file in write mode
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]  # Create a list of strings to write to the file
    file.writelines(lines)  # Write the list of strings to the file
"""

# 4. Closing a File:
# It's important to close a file after you're done working with it to free up system resources.
# You can close a file using the close() method, or by using a context manager (the with statement) which automatically handles closing the file for you.   
# Example while closing a file:
"""
file = open('example.txt', 'r')  # Open the file in read mode
content = file.read()  # Read the contents of the file
file.close()  # Close the file after you're done

with open('example.txt', 'r') as file:  # Open the file using a context manager
    content = file.read()  # Read the contents of the file
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
"""



#File Modes:
# When opening a file, you can specify the mode in which you want to open it.
# Here are some common file modes:
# 'r' - Read mode: Opens the file for reading (default mode). 
# The file must exist, otherwise an error will occur.

# 'w' - Write mode: Opens the file for writing. 
# If the file already exists, it will be truncated (i.e., all existing content will be deleted).
# If the file does not exist, a new file will be created.

# 'a' - Append mode: Opens the file for writing. 
# If the file already exists, new content will be added to the end of the file without deleting existing content.
# If the file does not exist, a new file will be created.


# 'x' - Exclusive creation mode: Opens the file for exclusive creation. 
# If the file already exists, an error will occur. If the file does not exist, a new file will be created.


# 'b' - Binary mode: Opens the file in binary mode (e.g., for non-text files like images or videos). 
# This can be combined with other modes (e.g., 'rb' for reading a binary file, 'wb' for writing a binary file).  

    
# 't' - Text mode: Opens the file in text mode (default mode). 
# This can be combined with other modes (e.g., 'rt' for reading a text file, 'wt' for writing a text file).


# 'U' - Universal newline mode: Opens the file with universal newline support. 
# This allows you to read files with different newline conventions (e.g., '\n', '\r\n', '\r') without having to worry about the specific newline characters used in the file.
# This mode is deprecated in Python 3, as universal newline support is now the default behavior when opening files in text mode. 

  
# '+' - Update mode: Opens the file for updating (reading and writing). 
# This can be combined with other modes (e.g., 'r+' for reading and writing a file, 'w+' for writing and reading a file, 
# 'a+' for appending and reading a file).  


# Write the function to write and read the file:
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content) 

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


result = write_to_file('example.txt', 'Hello, World!\nWelcome to file handling in Python.')
print(result)  # This will print None since the write_to_file function does not return anything
content = read_from_file('example.txt')
print(content)  # This will print the content of the file: "Hello, World!\  nWelcome to file handling in Python."

