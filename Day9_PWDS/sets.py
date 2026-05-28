# Sets operations:
# Sets are mutable, meaning you can add or remove elements from them, but they do not allow duplicate values.
# In sets, elements must be immutable (like numbers, strings, tuples), but the set itself is mutable.





#Frozen-sets:
# A frozenset is an immutable version of a set. 
# Once created, you cannot modify a frozenset (i.e., you cannot add or remove elements). 
# Frozen-sets are hashable, which means they can be used as keys in dictionaries or elements of other sets. 

# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 'apple', 'banana'])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 'apple', 'banana'})  

# frozensets support the same set operations as regular sets, 
# but since they are immutable, you cannot modify them after creation.
# Union
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
union_frozenset = frozenset1 | frozenset2 
print(union_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})


# Intersection
intersection_frozenset = frozenset1 & frozenset2
print(intersection_frozenset)  # Output: frozenset({3})
# Difference
difference_frozenset = frozenset1 - frozenset2  
print(difference_frozenset)  # Output: frozenset({1, 2})
# Symmetric Difference
symmetric_difference_frozenset = frozenset1 ^ frozenset2
print(symmetric_difference_frozenset)  # Output: frozenset({1, 2, 4, 5})

# Subset and Superset
frozenset3 = frozenset([1, 2])
print(frozenset3.issubset(frozenset1))  # Output: True
print(frozenset1.issuperset(frozenset3))  # Output: True


