# raising exception

class AgeError(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeError("You must be at least 18 years old.")

    print("Access granted!")

except AgeError as e:
    print("Error:", e)