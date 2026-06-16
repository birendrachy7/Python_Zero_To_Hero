# create subtract() with type hints


def subtract(a:int, b: int) -> int:
    # return f"subract from {a} from {b} is {b-a}"
    return b-a
print(subtract(5,6))


# Create a list of string
from typing import List
def greet(name: str) -> str:
    return f"Hello, {name}"

names: list[str] = ["Alice", "Bob", "Charlie"]
for name in names:
    print(greet(name))
    
# Create a dictionary of subject marks
subject_marks: dict[str, int] = {
    "Math": 90,
    "Science": 85,
    "English": 88
}

print(subject_marks)


# Create a function using Union
from typing import Optional, Union

def square(num: Union[int, float]) -> float:
    return num * num

print(square(5))
print(square(2.5))


# Create an Employee Class
class Employee:
    def __init__(self, emp_id: int, name: str, salary: int):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    
    def display(self)-> None:
        print("Emp Id: ", self.emp_id)
        print("Emp Name: ", self.name)
        print("Salary: ", self.salary)

emp1: tuple[int, str, float] = (101, "Alice", 50000.0)
print(emp1)




