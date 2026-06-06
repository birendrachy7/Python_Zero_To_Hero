class Vehicle:
    def show_info(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Create object of Car
c = Car()

# Call methods
c.show_info()
c.car_info()