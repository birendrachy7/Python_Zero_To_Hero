# Inheritance in Python
'''
## Introduction

Inheritance is one of the most important features of Object-Oriented Programming (OOP). It allows a new class to acquire the properties and methods of an existing class.

The existing class is called the **Parent Class**, **Base Class**, or **Super Class**.

The new class is called the **Child Class**, **Derived Class**, or **Sub Class**.

Inheritance promotes **code reusability** because the child class can use the attributes and methods of the parent class without rewriting them.

---

# Syntax of Inheritance


class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code


'''
# Example of Inheritance


class Person:
    def show(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()

s.show()
s.study()

'''
### Explanation

* Person is the parent class.
* Student is the child class.
* Student inherits the show() method from Person.
* Student can also have its own methods such as study().

---

# Why Use Inheritance?

1. Code Reusability
2. Easy Maintenance
3. Faster Development
4. Better Organization
5. Supports Hierarchical Classification

---

# Types of Inheritance in Python

Python supports five types of inheritance:

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance


# Advantages of Inheritance

1. Reusability of Code
2. Reduces Redundancy
3. Easy Maintenance
4. Faster Development
5. Better Program Structure
6. Supports Polymorphism

---

# Disadvantages of Inheritance

1. Increases program complexity.
2. Changes in parent class may affect child classes.
3. Deep inheritance can be difficult to understand.

'''