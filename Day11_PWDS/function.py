# Function in python:
# A function is a reusable block of code that performs a specific task. 
# It allows you to organize your code into manageable sections and promotes code reusability. 
# Functions can take input parameters, perform operations, and return output. 

#Defining a function:
# def keyword followed by the function name and parentheses.
# The function body is indented below the function definition.
# Example:
def greet(name):
    return f"Hello, {name}!"
#Calling a function:
# To call a function, you use the function name followed by parentheses, and pass any required arguments.
# Example: 
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with multiple parameters:
def add(a, b):
    return a + b

# Example usage:
result = add(5, 3)
print(result)  # Output: 8  



#Arguments and Parameters:
# Parameters are the variables defined in the function definition that accept values when the function is called.
# Arguments are the actual values passed to the function when it is called.
# Example 1:
def gret(greet_word,first_name,last_name):
  print(f"{greet_word} {first_name } {last_name}")
  print("Welcome")

gret("Hello","Birendra","Chaudhary")
gret("hi","Bibek", "Twari")
gret("Namaskar","Lochan", "Raja")

# Example 2:
def multiply(x, y):
    return x * y
# Calling the function with arguments
product = multiply(4, 5)
print(product)  # Output: 20



#Arguments:
# Positional Arguments: These are the most common type of arguments where the values are passed in the same order as the parameters defined in the function.
# Keyword Arguments: These arguments are passed by explicitly specifying the parameter name and its corresponding value, regardless of their position in the function definition.
# Default Arguments: These arguments have default values assigned to them in the function definition. If the caller does not provide a value for that parameter, the default value is used.
# Variable-length Arguments: These arguments allow you to pass a variable number of arguments to a function. They are defined using *args for non-keyword arguments and **kwargs for keyword arguments.
# Example of different types of arguments:
def example_function(positional_arg, keyword_arg='default', *args, **kwargs):
    print(f"Positional Argument: {positional_arg}")
    print(f"Keyword Argument: {keyword_arg}")
    print(f"Variable-length Arguments (args): {args}")
    print(f"Variable-length Keyword Arguments (kwargs): {kwargs}")
# Calling the function with different types of arguments
example_function('Hello', 'World', 1, 2, 3, key1='value1', key2='value2')


#Parameters:
# Parameters are the variables defined in the function definition that accept values when the function is called.
# Types of parameters:
# Positional Parameters: These parameters are defined in a specific order and must be provided in the same order when calling the function.
# Keyword Parameters: These parameters are defined with default values and can be provided in any order when calling the function, as long as the parameter names are specified.
# Example of different types of parameters:
def example_function(positional_param, keyword_param='default'):
    print(f"Positional Parameter: {positional_param}")
    print(f"Keyword Parameter: {keyword_param}")
# Calling the function with different types of parameters
example_function('Hello')  # Using default value for keyword_param
example_function('Hello', 'World')  # Providing a value for keyword_param
example_function(keyword_param='World', positional_param='Hello')  # Using keyword arguments to specify parameters in any order

