# Problem 2: Car Information
# Logic: Initialize attributes brand, color, and speed in the constructor.
# Use a method to neatly format and print all instance variables.
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Top Speed: {self.speed} km/h")
        print("-" * 20)

# Creating an object and displaying details
my_car = Car("Toyota", "Red", 180)
my_car.display_info()