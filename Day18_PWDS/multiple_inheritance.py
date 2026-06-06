# 2. Multiple Inheritance

## Definition

# When one child class inherits from more than one parent class, it is called Multiple Inheritance.

### Diagram

'''
Parent1   Parent2
    \      /
     \    /
      Child

'''

### Example


class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()
c.skill2()

'''
### Explanation

Child inherits methods from both Father and Mother.
'''