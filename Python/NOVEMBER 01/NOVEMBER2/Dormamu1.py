# Problem 5: Employee Salary Calculator
# Logic: Pass name and monthly_salary to __init__.
# Multiply monthly_salary by 12 inside the method to calculate and display the annual salary.
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def display_annual_salary(self):
        annual_salary = self.monthly_salary * 12
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: ${self.monthly_salary}")
        print(f"Annual Salary: ${annual_salary}")
        print("-" * 20)

# Creating an object and calling the method
emp = Employee("John Doe", 5000)
emp.display_annual_salary()