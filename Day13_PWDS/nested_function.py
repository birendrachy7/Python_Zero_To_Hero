#Nested Functions in Python:
# A nested function is a function defined inside another function. The inner function can access variables from the outer function's scope. This allows for encapsulation and can be useful for creating closures.  
# Basic Syntax of a Nested Function:
"""
def outer_function():
    # Code for the outer function
    def inner_function():
        # Code for the inner function
        pass or return statement for the inner function
        
    # More code for the outer function
    pass or return statement for the outer function

"""

#Key Characteristics of Nested Functions:
# Scope: The inner function can access variables from the outer function's scope, but the outer function cannot access variables from the inner function's scope.
# Accessing Outer Variables: The inner function can access and modify variables from the outer function's scope, which allows for powerful programming techniques such as closures.
# Encapsulation: Nested functions can help encapsulate functionality that is only relevant within the context of the outer function, preventing it from being accessed or modified from outside.
# Closures: If the inner function references variables from the outer function, it creates a closure
# Example of a nested function:
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 5
result = outer_function(10)
print(result)  # Output: 25