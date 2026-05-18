
# 1. KEYWORDS & BASIC INPUT/OUTPUT

# Keywords are reserved words with specific meanings in Python.
# print() is used to print data to the screen.
# input() is used to take input values from the user.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total_sum = num1 + num2
print("The sum of num1 and num2 is: ", total_sum)
print("Datatype: ", type(total_sum))

print("-" * 40)


# 2. STRING FORMATTING & ESCAPE SEQUENCES

user_name = str(input("Enter Your name: "))
user_age = int(input("Enter Your age: "))
user_salary = float(input("Enter Your salary: "))

# Basic print with newlines
print("\nName: ", user_name, "\nAge: ", user_age, "\nSalary: ", user_salary)

# format() method: inserts values into placeholders
print("The name of the user is {}. The age of the user is {}".format(user_name, user_age))

# f-strings: embed variables directly inside the string
print(f"User name is {user_name} and User Age is {user_age}")

# Escape Sequences
print("Hello \nWorld")        # \n (Newline): Breaks the text to the next line
print("hello \t world")       # \t (Tab): Inserts a horizontal tab space
print("hello \\ world")       # \\ (Backslash): Prints a literal backslash
print("He said, \"Hello\"")   # \" or \' (Quotes): Escapes internal quotes

print("-" * 40)


# 3. ARITHMETIC OPERATORS (PEMDAS)

user_num1 = int(input("Enter first number for math:\t")) 
user_num2 = int(input("Enter second number for math:\t"))

sum_result = user_num1 + user_num2
diff = user_num1 - user_num2
mul = user_num1 * user_num2
div = user_num1 / user_num2
mod = user_num1 % user_num2
exp = user_num1 ** user_num2  # ** is power (a^b)

print("The sum of the numbers is: ", sum_result)
print("The difference of the numbers is: ", diff)
print("The multiplication of the numbers is: ", mul)
print("The division of the numbers is: ", div)
print("The modulus of the numbers is: ", mod)
print("The exponentiation of the numbers is: ", exp)

print("-" * 40)


# 4. COMPARISON OPERATORS

x = 5
y = 6
print("Comparison Tests (x=5, y=6):")
print("x == y:", x == y)
print("x != y:", x != y)
print("x < y :", x < y)
print("x > y :", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

print("-" * 40)


# 5. ASSIGNMENT OPERATORS

a = 52
b = 1
print(f"Initial assignment -> a: {a}, b: {b}")

b += a
print("After += :", b)

b -= a
print("After -= :", b)

b *= a
print("After *= :", b)

b /= a
print("After /= :", b)

b %= a
print("After %= :", b)

b //= a
print("After //=:", b)

b **= a 
print("After **=:", b)

print("-" * 40)

# 6. LOGICAL OPERATORS (and, or, not)

log_x = True
log_y = False

print("log_x and log_y is:", log_x and log_y)
print("log_x or log_y is :", log_x or log_y)
print("not log_x is       :", not log_x)

# Truth Tables
print("\n--- 'and' Truth Table ---")
print("True and False :", True and False)
print("True and True  :", True and True)
print("False and False:", False and False)

print("\n--- 'or' Truth Table ---")
print("True or True  :", True or True)
print("True or False :", True or False)
print("False or False:", False or False)

print("\n--- 'not' Truth Table ---")
print("not True :", not True)
print("not False:", not False)

print("-" * 40)   # Visual Display


# 7. ADVANCED PRINT SYNTAX (sep & end)

print("apple", "ball", "cat", sep=",")
print("Python", "is", "fun", sep="-", end="!!!\n")
