#File Basics:
# A file is a collection of data stored on a computer. It can be a text file, a binary file, or any other type of file.
# A file have:
# 1. Name: The name of the file, including its extension (e.g., "example.txt").
# 2. Path: The location of the file on the computer (e.g., "C:/Users/Username/Documents/example.txt").
# 3. Size: The amount of data stored in the file, usually measured in bytes.    


# File Paths:
# A file path is a string that specifies the location of a file on your computer.

# There are two types of file paths:
# 1. Absolute Path: An absolute path specifies the complete path to a file, starting from the root directory 
# (e.g., "C:/Users/Username/Documents/example.txt").
 
# 2. Relative Path: A relative path specifies the path to a file relative to the current working directory 
# (e.g., "Documents/example.txt" if the current working directory is "C:/Users/Username").




# import os : is a module that provides a way of using operating system dependent functionality like reading or writing to the file system.
import os
os.chdir(r"C:\Users\infob\Documents")  # Change the current working directory to the specified path   
print("Changed working directory to: ", end="")  # Print the new current working directory
print(os.getcwd())  # Print the current working directory

print (os.listdir())  # List all files and directories in the current working directory 
os.mkdir("NewFolder1")  # Create a new directory named "NewFolder" in the current working directory
print (os.listdir())  # List all files and directories in the current working directory to confirm


os.rmdir("NewFolder1")  # Remove the directory named "NewFolder" from the current working directory
print (os.listdir())  # List all files and directories in the current working directory to confirm  
os.makedirs("NewFolder1/SubFolder")  # Create a new directory named "SubFolder" inside "NewFolder"
print (os.listdir())  # List all files and directories in the current working directory to confirm

os.removedirs("NewFolder1/SubFolder")  # Remove the directory "SubFolder" and its parent directory "NewFolder1"
print (os.listdir())  # List all files and directories in the current working directory to confirm  


os.readlink("example.txt")  # Read the target of a symbolic link named "example.txt"
os.symlink("example.txt", "example_link.txt")  # Create a symbolic link named   

file_pTH = os.path.join("C:", "Users", "infob", "Documents", "example.txt")  # Create a file path by joining directory names
print(file_pTH)  # Print the created file path

if os.path.exists(file_pTH):  # Check if the file at the specified path exists
    print("File exists.")  # Print a message if the file exists
else:
    print("File does not exist.")  # Print a message if the file does not exist 

paths = os.path.join(os.getcwd(), "example.txt")  # Create a file path by joining the current working directory and the file name
print(paths)  # Print the created file path
print("basename: ", os.path.basename(paths))  # Print the base name of the file (e.g., "example.txt )
print("dirname: ", os.path.dirname(paths))  # Print the directory name of the file (e.g., "C:/Users/infob/Documents")
print("split: ", os.path.split(paths))  # Split the file path into a tuple  
print("splitext: ", os.path.splitext(paths))  # Split the file path into a tuple (root, ext) where ext is the file extension