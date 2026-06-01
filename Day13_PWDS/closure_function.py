# Closure
# A closure is a function object that has access to variables in its lexical scope, even when the function is called outside of that scope.
# Closures are created when a nested function references variables from its enclosing scope. The inner function retains access to these variables, allowing it to use and modify them even after the outer function has finished executing.

#Key Characteristics of Closures:
# Access to Enclosing Scope: A closure can access variables from its enclosing scope, which allows it to maintain state and perform operations based on that state.
# Encapsulation: Closures can help encapsulate functionality and data, making it easier to manage and organize code.
# Use Cases: Closures are often used in scenarios such as data hiding, creating decorators, and implementing callback functions.
# State Retention: Closures can retain state across multiple calls, which can be useful for creating functions that need to remember information between calls.
# Returning Functions: Closures can be used to return functions that have access to the variables of the outer function, allowing for powerful programming techniques.
# Remember that a closure is not just a nested function; it is a nested function that captures and retains access to variables from its enclosing scope. This allows the inner function to maintain state and perform operations based on that state, even after the outer function has finished executing.

# Example of a closure:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
closure = outer_function(10)
result = closure(5)  # This will return 15, as the inner function has
# access to the variable 'x' from the outer function's scope.
print(result)  # Output: 15




# Another example of a closure:

def o(x):
  def i(y):
    return x+y
  return i
add_five= o(5)
print(add_five)

print(add_five(3))
print(add_five(6))


# A more practical example of a closure is a function that generates power functions. 
# The outer function takes a base as an argument and returns an inner function that takes a power as an argument and 
# raises the base to that power.

def power_raiser(base):

  def inner_function(power):
    return base ** power
  return inner_function

square = power_raiser(2)
cube = power_raiser(3)

print(square(4))
print(cube(2))