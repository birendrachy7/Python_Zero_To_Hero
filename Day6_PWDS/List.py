# List 
# Lists are ordered, mutable, and allow duplicate elements.
# Lists are a versatile data structure in Python that can hold a collection of items. 
# They are defined using square brackets [] and can contain elements of different data types, including numbers, strings, and even other lists. 
# Lists are ordered, meaning that the elements have a specific order and can be accessed using their index. 
# They are mutable, which means that you can modify the contents of a list after it has been created. 
# Additionally, lists allow duplicate elements, so you can have multiple occurrences of the same value in a list.
# Lists are commonly used for storing and manipulating collections of data in Python, and 
# they provide a wide range of built-in methods for performing various operations on the list elements.

# Creating a list
print("Creating a list:")
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing elements in a list
print("\nAccessing elements in a list:")
print(my_list[0])  # Output: 1 (accessing the first element)
print(my_list[2])  # Output: 3 (accessing the third element
print(my_list[-1])  # Output: 5 (accessing the last element)

# Modifying elements in a list
print("\nModifying elements in a list:")
# my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # Modifying the first element
print(my_list)  # Output: [10, 2, 3,
my_list[2] = 30  # Modifying the third element
print(my_list)  # Output: [10, 2, 30,
my_list[-1] = 50  # Modifying the last element
print(my_list)  # Output: [10, 2, 30, 4, 50]


# Key Characteristics of Lists:
# 1. Ordered: Lists maintain the order of elements as they were added. You can access elements by their index.
# 2. Mutable: Lists can be modified after they are created. You can add, remove, or change elements in a list.
# 3. Allow Duplicate Elements: Lists can contain duplicate elements. You can have multiple occurrences of the same value in a list. 


#Ordered: Lists maintain the order of elements as they were added. You can access elements by their index.

#Mutable: Lists can be modified after they are created. You can add, remove, or change elements in a list.

#Allow Duplicate Elements: Lists can contain duplicate elements. You can have multiple occurrences of the same value in a list.




#len() function is used to get the number of elements in a list.
# example of len() function:
print(f"Length of the list: {len(my_list)}")


# in operator is used to check if an element exists in a list. It returns True if the element is found, otherwise it returns False.
# It helps to check for the presence of an element in a list and can be used in conditional statements to perform actions based on whether the element exists or not.
# Syntax: element in list
print(10 in my_list)  # Output: True (10 is in the list)
print(5 in my_list)   # Output: False (5 is not in the list



# Indexing in Lists:
# Lists are indexed, meaning each element in a list has a specific position or index.
# The index of the first element is 0, the second element is 1, and so on. Negative indexing is also supported, where -1 refers to the last element, -2 to the second last, and so on.

# Positive Indexing:
my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list[0])  # Output: 'a' (first element)
print(my_list[2])  # Output: 'c' (third element)

# Negative Indexing:
my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list[-1])  # Output: 'e' (last element)
print(my_list[-3])  # Output: 'c' (third last element)

# Index error occurs when you try to access an index that is out of the range of the list. For example, if you have a list with 5 elements and you try to access the index 5 or higher, it will raise an IndexError because those indices do not exist in the list. Always ensure that the index you are trying to access is within the valid range of the list to avoid this error.
# my_list = [1, 2, 3, 4, 5]
# print(my_list[5])  # This will raise an IndexError because index 5 does not exist in the list (valid indices are 0 to 4)



# List Slicing:
# List slicing allows you to access a portion of a list by specifying a range of indices. 
# The syntax for slicing is list[start:stop:step], 
# where start is the index to begin slicing (inclusive), 
# stop is the index to end slicing (exclusive), 
# step is the interval between indices (optional).
# Default values for start is 0, for stop is the length of the list, and for step is 1.
# Negative indices can also be used in slicing to count from the end of the list.
# example of slicing a list:
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[1:4])  # Output: [2, 3, 4] (slicing from index 1 to 3)
print(my_list[:3])   # Output: [1, 2, 3] (slicing from the beginning to index 2)
print(my_list[2:])   # Output: [3, 4, 5] (slicing from index 2 to the end)
print(my_list[::2])  # Output: [1, 3, 5] (slicing with a step of 2)
print(my_list[::-1]) # Output: [5, 4, 3, 2, 1] (slicing with a step of -1 to reverse the list)  




#Modifying a list:
# my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # Modifying the first element    
print(my_list)  # Output: [10, 2, 3, 4, 5]
my_list[2] = 30  # Modifying the third element

#changing the multiple elements in a list using slicing
# my_list = [1, 2, 3, 4, 5]
my_list[1:4] = [20, 30, 40]  # Modifying elements from index 1 to 3
print(my_list)  # Output: [1, 20, 30, 40


#Adding Methods in lists:
# 1. append(): Adds an element to the end of the list.
#example of append() method:
my_list = [1, 2, 3]
my_list.append(4)  # Adding an element to the end of the list
print(my_list)  # Output: [1, 2, 3, 4]

# 2. insert(): Inserts an element at a specified index in the list.
# example of insert() method:
my_list = [1, 2, 3]
my_list.insert(1, 10)  # Inserting 10 at index 1
print(my_list)  # Output: [1, 10, 2, 3]

# 3. extend(): Extends the list by appending elements from another iterable (e.g., another list). 
# example of extend() method:
my_list = [1, 2, 3]
my_list.extend([4, 5])  # Extending the list with another list
print(my_list)  # Output: [1, 2, 3, 4, 5]






#Removing methods in lists:
# 1. remove(): Removes the first occurrence of a specified value from the list.
# example of remove() method:
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # Removing the first occurrence of 2
print(my_list)  # Output: [1, 3, 2, 4]

# 2. pop(): Removes and returns the element at a specified index (default is the last element) from the list.
# example of pop() method:
my_list = [1, 2, 3, 4, 5]   
popped_element = my_list.pop(2)  # Removing and returning the element at index 2
print(popped_element)  # Output: 3 (the element that was removed)
print(my_list)  # Output: [1, 2, 4, 5] (the list after removing the element)

# 3. clear(): Removes all elements from the list, resulting in an empty list.
# example of clear() method:
my_list = [1, 2, 3, 4, 5]
my_list.clear()  # Removing all elements from the list
print(my_list)  # Output: [] (the list is now empty)

# 4. del statement: The del statement can be used to remove an element at a specific index or to delete the entire list.
# example of del statement:
my_list = [1, 2, 3, 4, 5]   
del my_list[1]  # Removing the element at index 1
print(my_list)  # Output: [1, 3, 4, 5] (the list after removing the element)    



#Searching and  Counting in lists:
# 1. index(): Returns the index of the first occurrence of a specified value in the list. If the value is not found, it raises a ValueError.
# example of index() method:
my_list = [1, 2, 3, 4, 2]
index_of_2 = my_list.index(2)  # Finding the index of the first occurrence of 2
print(index_of_2)  # Output: 1 (the index of the first occurrence

# 2. count(): Returns the number of occurrences of a specified value in the list.
# example of count() method:
my_list = [1, 2, 3, 4, 2]
count_of_2 = my_list.count(2)  # Counting the occurrences of 2
print(count_of_2)  # Output: 2 (the number of occurrences of 2 in the list)


#Ordered methods in lists:
# 1. sort(): Sorts the elements of the list in ascending order by default.
# example of sort() method:
my_list = [3, 1, 4, 2, 5]
my_list.sort()  # Sorting the list in ascending order
print(my_list)  # Output: [1, 2, 3, 4, 5] (the list sorted in ascending order)

# 2. sorted(): Returns a new sorted list from the elements of the given iterable (e.g., list) without modifying the original list.
# example of sorted() function:
my_list = [3, 1, 4, 2, 5]
sorted_list = sorted(my_list)  # Creating a new sorted list
print(sorted_list)  # Output: [1, 2, 3, 4, 5] (the new sorted list)
print(my_list)  # Output: [3, 1, 4, 2, 5] (the original list remains unchanged)

# 3. reverse(): Reverses the order of the elements in the list in place (modifies the original list).   
# example of reverse() method:
my_list = [1, 2, 3, 4, 5]
my_list.reverse()  # Reversing the order of the list
print(my_list)  # Output: [5, 4, 3, 2, 1] (the list reversed in place)  




#List Comprehension:
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable (e.g., list) while optionally filtering items using a condition.
# The syntax for list comprehension is: [expression for item in iterable if condition]
# example of list comprehension:
# Creating a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]  # Generating squares of numbers from 1 to 5
print(squares)  # Output: [1, 4, 9, 16, 25] (the list of squares generated using list comprehension)

# Creating a list of even numbers using list comprehension with a condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]  # Generating even numbers from 1 to 10
print(even_numbers)  # Output: [2, 4, 6, 8, 10] (the list of even numbers generated using list comprehension with a condition)

# List comprehension can also be used to create a list of tuples or to apply more complex expressions. 
# It is a powerful and efficient way to generate lists in Python while keeping the code concise and readable.

#List Comprehension with condition:
# Creating a list of squares of even numbers using list comprehension with a condition
squares_of_even = [x**2 for x in range(1, 11) if x % 2 == 0]  # Generating squares of even numbers from 1 to 10
print(squares_of_even)  # Output: [4, 16, 36,   64, 100] (the list of squares of even numbers generated using list comprehension with a condition)     

