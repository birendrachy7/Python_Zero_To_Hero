class Teacher:
    def teach(self):
        print("Teaching students")

class Singer:
    def sing(self):
        print("Singing a song")

class Person(Teacher, Singer):
    pass

# Create object of Person
p = Person()

# Call methods
p.teach()
p.sing()