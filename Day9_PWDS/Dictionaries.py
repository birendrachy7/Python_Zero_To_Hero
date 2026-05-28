# Dictionaries are a collection of key-value pairs. They are unordered, mutable, and indexed.
# Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :.
# Creating a dictionary  by normal way
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating a dictionary using the dict() constructor
my_dict2 = dict(name='Bob', age=25, city='Los Angeles')
print(my_dict2)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# Creating a dictionary from a list of tuples
my_list_of_tuples = [('name', 'Charlie'), ('age', 35), ('city', 'Chicago')]
my_dict3 = dict(my_list_of_tuples)
print(my_dict3)  # Output: {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}

# Creating a dictionary from two lists using zip()
keys = ['name', 'age', 'city']
values = ['David', 40, 'Houston']
my_dict4 = dict(zip(keys, values))
print(my_dict4)  # Output: {'name': 'David', 'age': 40, 'city': 'Houston'}


# Accessing values in a dictionary
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 30
print(my_dict['city'])  # Output: New York

#get() method to access values
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('age'))   # Output: 30
print(my_dict.get('city'))  # Output: New York


#modifying values in a dictionary
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
my_dict.update({'city': 'San Francisco'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'San Francisco'}

#Adding new key-value pairs to a dictionary
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'San Francisco', 'country': 'USA'}


# Removing key-value pairs from a dictionary


del my_dict['age']
print(my_dict)  # Output: {'name': 'Alice', 'city': 'San Francisco', 'country': 'USA'}
my_dict.pop('city')

print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}
my_dict.clear()
print(my_dict)  # Output: {}


