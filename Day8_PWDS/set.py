#   Sets in python:
#   A set is an unordered collection of unique elements. 
#  It is defined using curly braces {} or the built-in set() function. Sets are mutable, meaning you can add or remove elements from them, 
# but they do not allow duplicate values.

#Sets are mutable, meaning you can add or remove elements from them, but they do not allow duplicate values.
# In sets, elements must be immutable (like numbers, strings, tuples), but the set itself is mutable.

# Creating a set
my_set = {1, 2, 3, 'apple', 'banana'}
print(my_set)  # Output: {1, 2, 3, 'apple', 'banana'}
# Creating an empty set


empty_set = set()
print(empty_set)  # Output: set()

# creating a set form an iterable
my_list = [1, 2, 3, 'apple', 'banana']
my_set_from_list = set(my_list)
print(my_set_from_list)  # Output: {1, 2, 3, 'apple', 'banana'}




#set operations:
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
# Difference
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
# Subset and Superset
set3 = {1, 2}
print(set3.issubset(set1))  # Output: True
print(set1.issuperset(set3))  # Output: True



# Adding and updating elements in a set
my_set.add('orange')    
print(my_set)  # Output: {1, 2, 3, 'apple', 'banana', 'orange'}
my_set.update([4, 5, 'grape'])
print(my_set)  # Output: {1, 2, 3, 'apple', 'banana', 'orange', 4, 5, 'grape'}

# removing elements from a set
my_set.remove('banana')
print(my_set)  # Output: {1, 2, 3, 'apple', 'orange'}
my_set.discard('grape')  # No error if 'grape' is not
print(my_set)  # Output: {1, 2, 3, 'apple', 'orange'}
my_set.pop()  # Removes and returns an arbitrary element
print(my_set)  # Output: Remaining elements in the set after pop    
my_set.clear()  # Removes all elements from the set
print(my_set)  # Output: set()  



