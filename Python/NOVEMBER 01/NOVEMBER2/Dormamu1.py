# Problem 8: Method Overriding in Vehicles
# Logic: Parent Vehicle has a generic start(). Car and Bike inherit and redefine start()
# to override the default behavior with their specific starting mechanisms.
class Vehicle:
    def start(self):
        print("The vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key ignition.")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a kick-start.")

# Creating objects and demonstrating overriding
generic_vehicle = Vehicle()
my_car = Car()
my_bike = Bike()

generic_vehicle.start()
my_car.start()
my_bike.start()
print("-" * 20)