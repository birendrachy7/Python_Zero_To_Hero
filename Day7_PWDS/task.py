# output
"""
apple start with a
apple has 5 letter
banana start with b
banana has 6 letter
cherry start with c
cherry has 6 letter
Grapes start with other than a
s,b,c
Grapes has 6 letter
"""

fruits = ['apple', 'banana', 'cherry', 'Grapes']
for fruit in fruits:
    print(f"{fruit} start with {fruit[0]}") 
    # why fruit[0] is used here?
    # fruit[0] is used to access the first character of the string 'fruit'. 
    # In Python, strings are indexed starting from 0, so fruit[0] gives us the first character of the string. 
    # For example, for 'apple', fruit[0] would return 'a', for 'banana' it would return 'b', and so on. 
    # This allows us to determine the starting letter of each fruit in the list.
    print(f"{fruit} has {len(fruit)} letter")
    