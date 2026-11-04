# Problem 1: Student Details
# Logic: Define a class with an __init__ constructor to initialize attributes.
# Create a method to print the details. Instantiate the class and call the method.
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")
        print("-" * 20)

# Creating an object and displaying details
student1 = Student("Alice", 101, "Computer Science")
student1.display_details()# Problem 3: Calculate the Area of a Rectangle
# Logic: Store length and breadth as instance variables.
# The calculate_area method multiplies them and returns the product based on Area = L * B.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

# Creating an object and displaying the output
rect = Rectangle(10, 5)
area = rect.calculate_area()
print(f"Area of the rectangle: {area}")
print("-" * 20)