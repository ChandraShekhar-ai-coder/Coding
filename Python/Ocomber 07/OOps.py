class Customer:
    def __init__(self, name, amount, payment_type):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type.upper()  # Ensures uppercase

    # This method must be indented inside the class
    def Show_Payment(self):
        print(f"Name : {self.name} \nAmount : {self.amount} \nPayment Mode : {self.payment_type}\n\n")

# Creating the object (instance) of the class
customer1 = Customer("Salman", 50000, "UPI")

# Calling the method to print details
customer1.Show_Payment()
