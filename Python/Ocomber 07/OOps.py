class Customer:
    def __init__(self, name, amount, payment_type):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type.upper()  # to make  uppercase

    def Show_Payment(self):
        print(f"Name : {self.name} \nAmount : {self.amount} \nPayment Mode : {self.payment_type}\n\n")
        
class payment_tracker:
    def __init__(self):
        self.customers=[]
    def add__customers(self,customer):
        self.customers.append(customer)
    def calculate_payment(self):
        total_cash = 0
        total_card = 0
        total_upi = 0


customer1 = Customer("Shekhar", 50000, "UPI")


customer1.Show_Payment()
 