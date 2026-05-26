# Tuples in Python
# Tuples are ordered, immutable collections of items in Python. Once a tuple is created, its elements cannot be changed (mutated).
# Creating a tuple
my_tuple = (1, 2, 3, 'apple', 'banana')
# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1 

#Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()


# Tuple operations

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)


# Repetition
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)


#Tuple packing
packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)


# Tuple unpacking
a, b, c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3



# Tuple methods
# count() - returns the number of occurrences of a specified value
print(my_tuple.count('apple'))  # Output: 1
# index() - returns the index of the first occurrence of a specified value
print(my_tuple.index('banana'))  # Output: 4

# Indexing and slicing
#Indexing:
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'apple'   

# Slicing:
print(my_tuple[1:4])  # Output: (2, 3, 'apple')
print(my_tuple[:3])   # Output: (1, 2, 3)
print(my_tuple[3:5])   # Output: ('apple', 'banana')



#Why Tuples are used?
# 1. Immutability: Tuples are immutable, which means that once they are created, their contents cannot be changed. This can be useful for ensuring that data remains constant and is not accidentally modified.
# 2. Performance: Tuples can be more memory-efficient than lists because they are immutable
# 3. Hashability: Tuples can be used as keys in dictionaries because they are hashable, while lists cannot be used as keys because they are mutable.
# 4. Multiple return values: Functions can return multiple values as a tuple, which can be convenient for returning related data together.



#Tuple enumerate() function
# The enumerate() function in Python is used to add a counter to an iterable and returns it as an enumerate object. This can be useful when you want to loop through an iterable and have access to both the index and the value of each item.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple    
# Index: 1, Fruit: banana


# tuple enumerate() with start parameter without for loop
# The enumerate() function also has an optional start parameter that allows you to specify the starting index for the enumeration. By default, the start parameter is set to 0, but you can change it to any integer value.
fruits = ['apple', 'banana', 'cherry']
enumerated_fruits = enumerate(fruits)
print(enumerated_fruits)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]