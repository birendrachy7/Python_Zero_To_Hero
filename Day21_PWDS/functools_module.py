#The functools module offers a collection of tools that simplify working with functions and callable objects. 
# It includes utilities to modify, extend or optimize functions without rewriting their core logic, 
# helping you write cleaner and more efficient code.


# Why do we need functools module?
# -> Provides higher-order functions and decorators that simplify functional programming tasks.
# -> Enables memoization using lru_cache() to speed up repeated function calls.
# -> Offers tools like partial() to fix certain arguments of a function and create simpler versions.
# -> Includes decorators like @total_ordering to reduce boilerplate when implementing rich comparisons.
# -> Helps write cleaner, more efficient and reusable code with minimal redundancy.



# Functions in functools Module
# 1. Partial class
# The partial class fix certain arguments of a function and create a new function with fewer parameters. This is especially useful for creating specialized versions of functions without defining new ones from scratch.

# Syntax:

# partial(func, /, *args, **keywords)

# Parameter:

# func: The original function to apply partially.
# *args: Positional arguments to fix from left to right.
# **keywords: Keyword arguments to fix by name.


import functools 
def power(a, b):
    return a ** b

pow2 = functools.partial(power, b=2) 
pow4 = functools.partial(power, b=4)  
power_of_5 = functools.partial(power, 5) 

print(power(2, 3))    
print(pow2(4))       
print(pow4(3))       
print(power_of_5(2))  

print(pow2.func)     
print(pow2.keywords) 
print(power_of_5.args)