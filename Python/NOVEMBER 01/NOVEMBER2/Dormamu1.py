# Problem 4: Simple Calculator
# Logic: Define a class with four methods. Each method takes two parameters 
# and performs the respective arithmetic operation. The division method handles zero division.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

# Creating an object and performing operations
calc = Calculator()
num1, num2 = 20, 5

print(f"Addition ({num1} + {num2}): {calc.add(num1, num2)}")
print(f"Subtraction ({num1} - {num2}): {calc.subtract(num1, num2)}")
print(f"Multiplication ({num1} * {num2}): {calc.multiply(num1, num2)}")
print(f"Division ({num1} / {num2}): {calc.divide(num1, num2)}")
print("-" * 20)