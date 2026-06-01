# Default and Keyword Arguments:
# Default Arguments: These are parameters that have a default value assigned to them in the function definition
# Keyword Arguments: These are arguments that are passed to a function by explicitly specifying the parameter name and its corresponding value, regardless of their position in the function definition.

# Example of Default and Keyword Arguments:
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
# Calling the function with default argument
greet("Alice")  # Output: Hello, Alice!


# Calling the function with a keyword argument
greet(name="Bob", greeting="Hi")  # Output: Hi, Bob!
# Calling the function with a positional argument and a keyword argument
greet("Charlie", greeting="Welcome")  # Output: Welcome, Charlie!
# Calling the function with a keyword argument and a positional argument
greet(greeting="Hey", name="David")  # Output: Hey, David!



# *args and **kwargs:
# *args allows you to pass a variable number of non-keyword arguments to a function
# *args is used to pass a variable number of non-keyword arguments to a function. 
# It allows you to handle situations where you don't know in advance how many arguments will be passed to the function. 
# The *args syntax collects all the positional arguments into a tuple, which can be accessed within the function.
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# Example of *args and **kwargs:
def example_function(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)
# Calling the function with variable-length arguments
example_function(1, 2, 3, key1='value1', key2='value2')
# Calling the function with only positional arguments
example_function(4, 5, 6)
# Calling the function with only keyword arguments
example_function(key3='value3', key4='value4')
