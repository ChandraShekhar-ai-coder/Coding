class Customer:
    def __init__(self, name, amount, payment_type):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type.upper()  # to make  uppercase

    def Show_Payment(self):
        print(f"Name : {self.name} \nAmount : {self.amount} \nPayment Mode : {self.payment_type}\n\n")


customer1 = Customer("Shw", 50000, "UPI")


customer1.Show_Payment()
