# Problem 3: """Create a class named `Rectangle` with attributes `length` 
# and `breadth`. Define a method named `calculate_area()` that calculates 
# and returns the area of the rectangle."""
# The calculate_area method multiplies them and
#  returns the product based on Area = L * B.
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