# An iterator is an object used to traverse through all the elements of a collection (lists, tuples, dictionaries) one element at a time.
# It follows the iterator protocol, which involves two key methods:

# __iter__(): Returns the iterator object itself.
# __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

# Need For Iterators
    # Lazy Evaluation: Processes items only when needed, saving memory.
    # Generator Integration: Pairs well with generators and functional tools.
    # Stateful Traversal: Keeps track of where it left off.
    # Uniform Looping: Same for loop works for lists, strings and more.
    # Composable Logic: Easily build complex pipelines using tools like itertools.

# Creating a Custom Iterator
    # Creating a custom iterator in Python involves defining a class that implements the __iter__() and __next__() methods

# Steps to follow:
    # 1. Define the Class: Start by defining a class that will act as the iterator.
    # 2. Initialize Attributes: In the __init__() method of the class, initialize any required attributes that will be used throughout the iteration process.
    # 3. Implement __iter__(): This method should return the iterator object itself. This is usually as simple as returning self.
    # 4. Implement __next__(): This method should provide the next item in the sequence each time it's called.
    
    
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.limit:
            raise StopIteration

        x = self.n
        self.n += 2
        return x


# Create an iterator for even numbers up to 10
even = EvenNumbers(10)

for num in even:
    print(num)