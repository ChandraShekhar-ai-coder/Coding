class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to display the employee's details
    def display_details(self):
        print("--- Employee Details ---")
        print(f"Name   : {self.name}")
        print(f"Salary : ₹{self.salary:,}") # Formats the number with commas

# Example usage:
if __name__ == "__main__":
    # Creating an object instance of the Employee class
    emp1 = Employee("Rahul Sharma", 75000)
    
    # Calling the method to display details
    emp1.display_details()
