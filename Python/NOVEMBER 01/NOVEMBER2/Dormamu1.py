# Problem 1: Student Details
"""Create a class named `Student` with attributes for the student's name, roll number, and course. Create an object of the class and display the student's details."""
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
student1.display_details()