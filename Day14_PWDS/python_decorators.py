# Python Decorators:
# A decorator is a design pattern in Python that allows you to modify the behavior of a function or a class method without changing its source code. 
# Decorators are often used to add functionality to existing code in a clean and maintainable way.
# A decorator is a function that takes another function as an argument 
# and returns a new function that typically extends the behavior of the original function.
# They follow the principle of "Don't Repeat Yourself" (DRY) by allowing you to reuse code across multiple functions without modifying their source code.
# The syntax for using a decorator is to prefix the function definition with the @ symbol followed by the decorator function name.
# Syntax:
# @decorator_function
# def original_function():
#     # Function body
# This is a sugar syntax that is equivalent to:
"""# def original_function():
#     # Function body
# original_function = decorator_function(original_function)
"""
# Example of a simple decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper  
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.




# Example of a decorator with arguments:
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator    
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!



# Example of a class method decorator:
def log_method_call(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper
class MyClass:
    @log_method_call
    def my_method(self, x):
        print(f"Inside my_method with argument {x}")
obj = MyClass()
obj.my_method(10)   
# Output:
# Calling method my_method with arguments (10,) and keyword arguments {}
# Inside my_method with argument 10
