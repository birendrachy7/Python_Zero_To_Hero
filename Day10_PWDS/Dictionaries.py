# Dictionary methods for merging and updating:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Using the update() method to merge dict2 into dict1
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
# Using the | operator to merge dictionaries (Python 3.9+)
merged_dict = dict1 | dict2 
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}


#Dictionary Views:
# Dictionary views provide a dynamic view of the dictionary's keys, values, and items. They are not lists but can be iterated over and support set operations.
# Types of dictionary views and Creating a dictionary Views:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Keys view
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])
# Values view
values_view = my_dict.values()
print(values_view)  # Output: dict_values(['Alice', 30, 'New York'])
# Items view
items_view = my_dict.items()
print(items_view)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])



#Looping through a dictionary:
# Looping through a dictionary allows you to access its keys, values, or key-value pairs. You can use a for loop to iterate over the dictionary.
# Looping through keys
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key in my_dict:
    print(key)  # Output: name, age, city   
# Looping through values
for value in my_dict.values():
    print(value)  # Output: Alice, 30, New York
# Looping through key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name Alice, age 30, city New York  



#Dictionary comprehensions:
# Dictionary comprehensions provide a concise way to create dictionaries. They consist of an expression followed by a for clause, and optionally, one or more if clauses.
# Creating a dictionary using a comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Creating a dictionary with a condition 
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


#Transforming an exiting dictionary using comprehensions:
# Given a dictionary of names and ages, create a new dictionary that categorizes people as 'Adult' or 'Minor' based on their age.
ages = {'Alice': 30, 'Bob': 15, 'Charlie': 25, 'David': 10}
age_category = {name: 'Adult' if age >= 18 else 'Minor' for name, age in ages.items()}
print(age_category)  # Output: {'Alice': 'Adult', 'Bob': 'Minor', 'Charlie': 'Adult', 'David': 'Minor'}




#Filtering a dictionary using comprehensions:
# Given a dictionary of products and their prices, create a new dictionary that only includes products that cost more than $20.
products = {'Laptop': 999, 'Mouse': 25, 'Keyboard': 45, 'Monitor': 150, 'USB Cable': 10}
expensive_products = {product: price for product, price in products.items() if price > 20}
print(expensive_products)  # Output: {'Laptop': 999, 'Mouse': 25, 'Keyboard': 45, 'Monitor': 150}



#Reversing a dictionary using comprehensions:
# Given a dictionary of country-capital pairs, create a new dictionary that reverses the keys and values.
countries = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'India': 'New Delhi'}
reversed_countries = {capital: country for country, capital in countries.items()}   
print(reversed_countries)  # Output: {'Washington, D.C.': 'USA', 'Paris': 'France', 'Tokyo': 'Japan', 'New Delhi': 'India'}





#Nested dictionary:
employee = {
    'Alice': {
        'age': 30, 'department': 'HR'
        },
    'Bob': {
        'age': 25, 'department': 'IT'
        }
}

# Accessing nested dictionary values
print(employee['Alice']['age'])  # Output: 30

#get() method for nested dictionary
print(employee.get('Bob', {}).get('department', 'Not Found'))  # Output:

#Adding a new employee to the nested dictionary
employee['Charlie'] = {'age': 28, 'department': 'Finance'}
print(employee)

#Modifying an existing employee's department
employee['Alice']['department'] = 'Finance'
print(employee)

#Adding a new key-value pair to an existing employee
employee['Bob']['salary'] = 50000
print(employee)


#Looping through a nested dictionary:
for employee_name, details in employee.items():
    print(f"Employee Name: {employee_name}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
        