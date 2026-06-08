class AgeError (Exception):
    """Raise when age is invalid"""
    def __init__(self,age, message="Age must be between 0 and 120"):
        self.age=age
        self.message=message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} Invalid Age:{self.age}"

#Using the custom exception
def check_age(age):
    if age<0 or age >120:
        raise AgeError(age)
    print(f"Age {age} is valid")
try:
    age=int(input("Enter your age:\t"))
    check_age(age)

#User input
except ValueError:
    print("Please enter a valid age")
except AgeError as e:
    print(e)