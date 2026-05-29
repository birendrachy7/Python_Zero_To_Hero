#Task 1: Dictionary Looping and Comprehensions

#Output:
"""
The capital of Nepal is Kathmandu
The capital of India is New Delhi
The capital of USA is Washington, D.C.
The capital of Japan is Tokyo """


capital={
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "Japan": "Tokyo"
}


for key, value in capital.items():
    print(f"The capital of {key} is {value}")
    
    
#using loop statement to print only the keys of the dictionary
for key in capital.keys():
    print(key)
#using loop statement to print only the values of the dictionary
for value in capital.values():
    print(value)


#task 2 : same question
for key, value in capital.items():
    if key=="Nepal":
        print(f"The capital of {key} is {value}")