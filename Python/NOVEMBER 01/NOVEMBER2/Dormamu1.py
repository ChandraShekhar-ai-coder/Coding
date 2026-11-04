# Problem 3: Calculate the Area of a Rectangle
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