# -------- Loops in Python --------
# Loops are used to execute a block of code repeatedly until a certain condition is met.
# Purpose of loops:
# 1. To execute a block of code repeatedly until a certain condition is met.
# 2. To iterate over a sequence (like a list, tuple, string) or other iterable objects.
# 3. To perform a task multiple times without having to write the same code again and again.
# 4. To automate repetitive tasks and reduce the chances of errors in the code.
# 5. To improve the efficiency of the code by reducing the number of lines of code and making it more readable.

# In Python, we have the following types of loops:
# 1. for loop
for num in [1, 2, 3, 4, 5]:
    print(num, sep=",")

# Range function is used to generate a sequence of numbers. 
# It takes three parameters: start, stop, and step. 
# range(stop) - generates numbers from 0 to stop (exclusive)
# range(start, stop) - generates numbers from start to stop (exclusive)
# range(start, stop, step) - generates numbers from start to stop (exclusive) with a step of step.
# The start parameter is the starting number of the sequence, the stop parameter is the ending number of the sequence (exclusive), 
# and the step parameter is the increment between each number in the sequence. 
# If the step parameter is not provided, it defaults to 1.


i=2


for i in range(2, 21):   # range(start, stop) - generates numbers from start to stop 
    print(i) 
    
print(range(2, 21)) # This will generate numbers from 2 to 20 (exclusive of 21)



# 2. while loop





        
#getting indecx and items together using enumerate
#example of enumerate function:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
    

#looping through characters in a string
# example of looping through characters in a string:
my_string = "Hello, World!"
for char in my_string:
    print(char)
    

#count number of vowels in a string
user_string = input("Enter a string to count the number of vowels: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_string:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")


# .lower() method is used to convert a string to lowercase. It returns a new string with all the characters in lowercase.
# .upper() method is used to convert a string to uppercase. It returns a new string with all the characters in uppercase.

user_menu =str(input("Enter Your string to check vowels: "))

count=0
for yoyo in user_menu:
  if yoyo.lower() in "aeiou":
    count=count +1
print(count)

# break statement is used to exit a loop prematurely when a certain condition is met. 
# It is used to break out of the loop when a specific condition is true, 
# and the code after the break statement will not be executed.
#example of break statement
for num in range(1, 10):
    if num == 5:
        break
    print(num)


# continue statement is used to skip the current iteration of a loop and move on to the next iteration. 
# It is used to skip the rest of the code inside the loop for the current iteration when a specific condition is true, 
# and the loop will continue with the next iteration.
#example of continue statement:
for num in range(1, 10):
    if num == 5:
        continue
    print(num)




# pass statement is a null statement in Python. It is used as a placeholder for future code. 
# It is used when a statement is required syntactically but you do not want any code to be executed.
#example of pass statement:
for num in range(1, 10):
    if num == 5:
        pass
    print(num)
    