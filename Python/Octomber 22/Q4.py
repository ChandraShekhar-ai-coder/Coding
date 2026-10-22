class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    
    def display_details(self):
        print("--- Employee Details ---\n")
        print(f"Name   : {self.name}")
        print(f"Salary : ₹{self.salary:,}") 



