# What Are Generator Expressions
# A generator expression is a shorter and more compact way to create a generator without using a function or yield. 
# It looks similar to a list comprehension, but uses parentheses () instead of brackets [].

# Key Characteristics
    # Produces items one at a time (lazy evaluation).
    # Does not store all values in memory like a list comprehension does.
    # Ideal when you only need to iterate through the values once.
    # Returns a generator object, not a list.
    # Faster and more memory-efficient for large data sets.

# Syntax

# (expression for element in iterable if condition)


square_gen = (x**2 for x in range(10))

print(square_gen)

for i in square_gen:
    print(i)