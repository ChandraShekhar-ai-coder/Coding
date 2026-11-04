# ==========================================
# Level 1: Basics of Classes and Objects
# ==========================================

# Problem 1: Student Details
"""
Explanation:
We define a class `Student` using the `class` keyword. 
The `__init__` method is the constructor that initializes the attributes 
(name, roll_number, course) when an object is created. 
Finally, we create an object `student1` and print its attributes to display the details.
"""
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

# Creating an object of the Student class
student1 = Student("Aarav Sharma", 101, "Computer Science")

# Displaying the details
print("--- Problem 1: Student Details ---")
print(f"Name: {student1.name}")
print(f"Roll Number: {student1.roll_number}")
print(f"Course: {student1.course}\n")


# Problem 2: Car Information
"""
Explanation:
Similar to Problem 1, we define a `Car` class with an `__init__` constructor 
to set up the `brand`, `color`, and `speed` attributes. We instantiate `my_car` 
and print the stored data.
"""
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed  # speed in km/h

# Creating an object of the Car class
my_car = Car("Tata Motors", "Dark Edition Black", 180)

# Displaying the car's details
print("--- Problem 2: Car Information ---")
print(f"Brand: {my_car.brand}")
print(f"Color: {my_car.color}")
print(f"Top Speed: {my_car.speed} km/h\n")


# Problem 3: Calculate the Area of a Rectangle
"""
Explanation:
We define a `Rectangle` class with length and breadth attributes. 
We add a custom method `calculate_area` that uses the formula Length * Breadth.
It returns the computed value which we then print.
"""
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        # Formula: Area = Length × Breadth
        return self.length * self.breadth

# Creating an object and calling the method
rect = Rectangle(10, 5)
area = rect.calculate_area()

print("--- Problem 3: Rectangle Area ---")
print(f"Length: {rect.length}, Breadth: {rect.breadth}")
print(f"Area of the rectangle: {area}\n")


# ==========================================
# Level 2: Methods and Constructors
# ==========================================

# Problem 4: Simple Calculator
"""
Explanation:
The `Calculator` class contains four separate methods for basic arithmetic operations.
Each method takes two parameters (num1, num2) and returns the result.
Division includes a simple check to prevent ZeroDivisionError.
"""
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2

# Creating a calculator object
calc = Calculator()
n1, n2 = 15, 3

print("--- Problem 4: Simple Calculator ---")
print(f"Addition ({n1} + {n2}): {calc.add(n1, n2)}")
print(f"Subtraction ({n1} - {n2}): {calc.subtract(n1, n2)}")
print(f"Multiplication ({n1} * {n2}): {calc.multiply(n1, n2)}")
print(f"Division ({n1} / {n2}): {calc.divide(n1, n2)}\n")


# Problem 5: Employee Salary Calculator
"""
Explanation:
The `Employee` class uses a constructor to initialize the name and monthly salary.
The `calculate_annual_salary` method computes the annual salary by multiplying 
the monthly salary by 12, then formats and displays the result directly.
"""
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        annual_salary = self.monthly_salary * 12
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: ₹{self.monthly_salary}")
        print(f"Annual Salary: ₹{annual_salary}")

print("--- Problem 5: Employee Salary ---")
emp = Employee("Priya", 55000)
emp.calculate_annual_salary()
print()


# Problem 6: Bank Account Management
"""
Explanation:
The `BankAccount` class holds a balance and account holder name.
- `deposit` increases the balance.
- `withdraw` checks if the requested amount is less than or equal to the balance 
  to prevent overdrafting.
- `display_balance` simply prints the current state.
"""
class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Failed to withdraw ₹{amount}: Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}. Remaining Balance: ₹{self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.name} | Current Balance: ₹{self.balance}")

print("--- Problem 6: Bank Account ---")
account = BankAccount("Rohan", 2000)
account.display_balance()
account.deposit(1500)
account.withdraw(5000) # Should fail
account.withdraw(1000)
account.display_balance()
print()


# ==========================================
# Level 3: Inheritance, Encapsulation, Polymorphism
# ==========================================

# Problem 7: Animal Sounds Using Inheritance
"""
Explanation:
`Animal` is the parent (base) class containing the `eat` method. 
`Dog` and `Cat` are child (derived) classes that inherit from `Animal`. 
Therefore, they can use `eat()`, but they also define their own unique `sound()` methods.
"""
class Animal:
    def eat(self):
        print("This animal is eating.")

# Dog inherits from Animal
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof! Woof!")

# Cat inherits from Animal
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow! Meow!")

print("--- Problem 7: Animal Inheritance ---")
dog = Dog()
cat = Cat()

dog.eat()    # Inherited method
dog.sound()  # Child's own method

cat.eat()    # Inherited method
cat.sound()  # Child's own method
print()


# Problem 8: Method Overriding in Vehicles
"""
Explanation:
`Vehicle` defines a generic `start` method. 
`Car` and `Bike` inherit from `Vehicle` but provide their own implementation of `start()`. 
This replaces (overrides) the parent's method when called on child objects.
"""
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key turn: Vroom Vroom!")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a kick/button: Rev Rev!")

print("--- Problem 8: Method Overriding ---")
generic_vehicle = Vehicle()
my_car = Car()
my_bike = Bike()

generic_vehicle.start()
my_car.start()   # Overridden method
my_bike.start()  # Overridden method
print()


# Problem 9: Student Marks Validation Using Encapsulation
"""
Explanation:
We use Encapsulation by making the `__marks` attribute private (using double underscores). 
This prevents direct modification from outside the class. 
We provide controlled access using `set_marks` (setter) which validates the input 
and `get_marks` (getter) to retrieve the value.
"""
class StudentMarks:
    def __init__(self, name):
        self.name = name
        self.__marks = 0  # Private attribute

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks successfully updated to {marks} for {self.name}.")
        else:
            print(f"Invalid input: {marks}. Marks must be strictly between 0 and 100.")

    def get_marks(self):
        return self.__marks

print("--- Problem 9: Encapsulation ---")
student2 = StudentMarks("Kavya")
student2.set_marks(85)   # Valid
student2.set_marks(105)  # Invalid, will be rejected
student2.set_marks(-10)  # Invalid, will be rejected

print(f"Final retrieved marks for {student2.name}: {student2.get_marks()}")
print()


# Problem 10: Payment System Using Polymorphism
"""
Explanation:
Polymorphism allows different objects to respond to the same method call (`pay`) 
in their own unique way. We loop through a list of different payment objects 
and call `.pay()` on each. Python dynamically resolves which class's method to execute.
"""
class Payment:
    def pay(self, amount):
        print(f"Processing a generic payment of ₹{amount}")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}. Requesting PIN...")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing Card payment of ₹{amount}. Swiping card...")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Processing Cash payment of ₹{amount}. Handing over the bills...")

print("--- Problem 10: Polymorphism ---")
# Creating objects of different classes
payment_methods = [
    UPIPayment(), 
    CardPayment(), 
    CashPayment()
]

# Demonstrating polymorphism: calling the same method on different objects
bill_amount = 500
for method in payment_methods:
    method.pay(bill_amount)