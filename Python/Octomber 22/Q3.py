class rectangle:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath

    def rectangle_details(self):
        print("--- Rectangle Details   ---\n")
        print(f"Rectangle length = {self.length}")
        print(f"Rectangle Breath = {self.breath}"
    def calculate_area(self):
        return self.length * self.breadth        


rectangle1 = rectangle("Rahul Sharma", "2026BTCS042")
rectangle1.rectangle_details()





# Create an object
rect = Rectangle(10, 5)

# Display the area
print("Area of Rectangle:", rect.calculate_area())