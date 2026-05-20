# --- Conditionals Statements ----
#   Conditional statements are used to perform different actions based on different conditions.
#   They allow code to make decision based on the condition provided.
#   They execute a block of code if a specified condition is true. If the condition is false, another block of code can be executed.
#   In Python, we have the following conditional statements:
"""

# --- if statement ---
# They are used to execute a block of code if a specified condition is true. If the condition is false, the block of code will be skipped.
# Syntax:
# if condition:
#     # block of code to be executed if the condition is true

# WAP to check if the number is positive or negative or zero using if statement
print("#---- if statement ----#")
num1 = int(input("Enter a number: "))

if num1 > 0:
    print("The number is positive ")
if num1 < 0:
    print("The number is negative ")
if num1 == 0:
    print("The number is zero")


# --- if-else statement ---
# They are used to execute a block of code if a specified condition is true. If the condition is false, another block of code will be executed.
# Syntax:
# if condition:
# block of code to be executed if the condition is true
# else:
# block of code to be executed if the condition is false

print("#---- if-else statement ----#")
if num1 > 0:
    print("The number is positive ")
else:
    if num1 < 0:
        print("The number is negative ")
    else:
        print("The number is zero")


# --- if-elif-else statement ---
# They are used to execute a block of code if a specified condition is true. If the condition is false, another block of code will be executed.
# If there are multiple conditions to be checked, we can use the elif statement to check for additional conditions
# Syntax:
# if condition1:
# block of code to be executed if condition1 is true
# elif condition2:
# block of code to be executed if the condition1 is false and condition2 is true
# else:
# block of code to be executed if the condition1 is false and condition2 is false
print("#---- if-elif-else statement ----#")
if num1 > 0:
    print("The number is positive ")
elif num1 == 0:
    print("The number is zero ")
else:
    print("The number is negative")


# Create a simple calculator that performs the different operations based on the user input
user_a = int(input("Enter the value of num1 :"))
user_b = int(input("Enter the value of num2 :"))
user_operation = str(input("Enter the operation that want to calculate : "))

if user_operation == "+":
    print("The sum of num1 and num2 is : ", (user_a + user_b))
elif user_operation == "-":
    print("The difference of num1 and num2 is : ", (user_a - user_b))
elif user_operation == "*":
    print("The product of num1 and num2 is : ", (user_a * user_b))
elif user_operation == "/":
    print("The division of num1 and num2 is : ", user_a / user_b)
elif user_operation == "%":
    print("The modulus of num1 and num2 is : ", user_a % user_b)
elif user_operation == "**":
    print("The exponent of num1 and num2 is : ", user_a**user_b)
else:
    print("Invalid operation and re-enter the operation")


# Example of nested if statement
# WAP to check if the number is positive or negative or zero using nested if statement
print("#---- nested if statement ----#")
num2 = int(input("Enter a number: "))

if num2 >= 0:
    if num2 == 0:
        print("The number is zero ")
    else:
        print("The number is positive ")
else:
    print("The number is negative ")


# Syntax error for python occurs when the code is not written in the correct syntax.
# It is a common error that occurs when the code is not written in the correct format.
# It can be caused by missing parentheses, missing colons, or incorrect indentation.


# WAP to check the grade of the student based on the marks obtained.
user_grade = int(input("Enter your grade:"))

if user_grade > 90:
    print("Grade A")
elif user_grade >= 85 and user_grade <=90:
    print("Grade A-")
elif user_grade > 80:
    print("Grade B")
elif user_grade >= 75 and user_grade <= 80:
    print("Grade B-")
elif user_grade > 70:
    print("Grade C") 
elif user_grade >= 65 and user_grade <= 70:
    print("Grade C-")
elif user_grade > 60:
    print("Grade D")
else:
    print("Grade F")


"""
#COnditional statements (Ternary operator)
# Ternary operator is a one line if-else statement that is used to assign a value to a variable based on a condition.
# Syntax:   
# variable = value_if_true if condition else value_if_false
today_temperature = int(input("Enter the temperature: "))
weather = "Hot" if today_temperature > 20 else "Cold"
print("Today's weather is : ", weather)


user_grade = int(input("Enter your grade: "))
grade = "Pass" if user_grade >=45 else "Fail"
print("You are: ",grade)


#truthy and falsy values in python
# In Python, we have the concept of truthy and falsy values.
# Truthy values are values that are considered true in a boolean context. They include:
# 




#Round off method in python:
 
#round() used to round a number to a specified number of decimal places. 
# It takes two arguments: the number to be rounded and the number of decimal places to round to.
#example:
num1 = 3.141592653589793    
print("The value of pi is : ", round(num1, 2))   #Round to 2 decimal places

# round off using f-string method is used to round a number to a specified number of decimal places. 
# It takes two arguments: the number to be rounded and the number of decimal places to round to.

num3 = 3.141592653589793
print(f"The value of pi is : {num3:.5f}")   # Round to 5 decimal places   


