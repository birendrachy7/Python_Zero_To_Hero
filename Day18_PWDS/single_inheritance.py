# 1. Single Inheritance

## Definition

# When one child class inherits from one parent class, it is called Single Inheritance.

### Diagram
'''
Parent
   |
 Child

'''


### Example


class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.eat()
d.bark()