# Use map to convert all string in ["apple","banana","cherry"] to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = map(str.upper, fruits)
print(list(upper_fruits))