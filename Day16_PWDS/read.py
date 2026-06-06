# creating a fi;le and writing to it:
with open('example.txt', 'w') as file:  # Open the file in write mode
    file.write("Hello, World!\n")  # Write a string to the file
    file.write("Welcome to file handling in Python.\n")  # Write another string to the file
# reading from the file:
with open('example.txt', 'r') as file:  # Open the file in read
    # content = file.read()  # Read the entire contents of the file
    line = file.readline()  # Read a single line from the file
    # .readline() reads a single line from the file, while .readlines() reads all lines and returns them as a list of strings.
    
    # print(content)  # Print the contents of the file
    print(line)  # Print the line from the file

print("---------------------------------------------")
# Reading all lines of the file into a list:
with open('example.txt', 'r') as file:  # Open the file in read mode
    lines = file.readlines()  # Read all lines of the file into a list
    print(lines)  # Print the list of lines from the file
print("---------------------------------------------")
# Reading file by line using a loop:
with open('example.txt', 'r') as file:  # Open the file in read mode
    for line in file:  # Iterate through each line in the file
        print(line)  # Print each line from the file