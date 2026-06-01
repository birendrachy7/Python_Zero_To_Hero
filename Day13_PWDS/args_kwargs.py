# *args
# *args allows you to pass a variable number of non-keyword arguments to a function. 
# When you use *args in a function definition, it collects all the positional arguments into a tuple, which can be accessed within the function.
# It allows you to handle situations where you don't know in advance how many arguments will be passed to the function. 
# The *args syntax collects all the positional arguments into a tuple, which can be accessed within the function.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total    
# Example usage of *args
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15




# **kwargs (Arbitrary Keyword Arguments):
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# When you use **kwargs in a function definition, 
# it collects all the keyword arguments into a dictionary, which can be accessed within the function.
# The **kwargs syntax collects all the keyword arguments into a dictionary, which can be accessed within the function.
# The name kwargs is a convention, and you can choose any name you like, but it is commonly used to indicate that the function accepts arbitrary keyword arguments.
# Example of **kwargs:
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Example usage of **kwargs
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice



def save_user(**user):
    print(user)
save_user(id=1, name="Biru", age =22, email="biru@gmail.com")


#Create a function name book_detail that takes **kwargs
# output: Harry Potter was written by J.K. Rowling
def book_detail(**details):
    title = details.get('title', 'Unknown Title')
    author = details.get('author', 'Unknown Author')
    print(f"{title} was written by {author}")
# Example usage of the book_detail function
book_detail(title="Harry Potter", author="J.K. Rowling")
# Output: Harry Potter was written by J.K. Rowling

# Example usage of the book_detail function with missing arguments
book_detail(title="The Great Gatsby")
# Output: The Great Gatsby was written by Unknown Author

# another method to write the same function
def book_detail(title="Unknown Title", author="Unknown Author"):
    print(f"{title} was written by {author}")   
# Example usage of the book_detail function
book_detail(title="Harry Potter", author="J.K. Rowling")
# Output: Harry Potter was written by J.K. Rowling

# another method to write the same function without get()
def book_detail(**details):
    title = details['title'] if 'title' in details else 'Unknown Title'
    author = details['author'] if 'author' in details else 'Unknown Author'
    print(f"{title} was written by {author}")   
# Example usage of the book_detail function
book_detail(title="Harry Potter", author="J.K. Rowling")