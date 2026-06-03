# Scope in python:
# Scope in Python refers to the region of a program where a variable is defined and can be accessed. 
# It determines the visibility and lifetime of variables. 


# There are four types of scopes in Python:
# 1. Local Scope : Names defined inside a function are in the local scope of that function. 
# They can only be accessed within that function and are not visible outside of it.
# keyword local is used to refer to variables in the local scope from within a nested function.
#Syntax:
""" def outer_function():
       def inner_function(): 
#         local_variable = "Local Scope"
#         print(local_variable)  # Accessing variable from local scope
#     inner_function()
"""

# 2. Enclosing Scope : Names defined in an enclosing function are in the enclosing scope. 
# They can be accessed by the inner function but not by the outer function.
# Keyword nonlocal is used to refer to variables in the enclosing scope from within a nested function.
#Syntax:
"""# def outer_function():
#     x = "Enclosing Scope"
#     def inner_function():
#         nonlocal x
#         print(x)  # Accessing variable from enclosing scope
#     inner_function()
"""
# 3. Global Scope : Names defined at the top level of a module are in the global scope. 
# They can be accessed from anywhere within the module.
# Keyword global is used to refer to variables in the global scope from within a function.
#Syntax:
"""# global_variable = "Global Scope"   
# def my_function():
#     global global_variable
#     print(global_variable)  # Accessing variable from global scope
# my_function()
"""



# 4. Built-in Scope : Names defined in the built-in namespace are in the built-in scope. 
# They are always available and can be accessed from anywhere in the program.
#keyword builtins is used to refer to variables in the built-in scope from within a function.
#Syntax:
"""# import builtins
# def my_function():
#     print(builtins.len)  # Accessing built-in function from built-in scope
# my_function()
"""
# Example of built-in scope:
# print() is a built-in function that is available in the built-in scope.


#Local Scope:
# Local scope refers to the variables that are defined within a function. 
# These variables are only accessible within that function and cannot be accessed outside of it.