class Customer:
    def __init__(self,name,amount,payment_type):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type.upper()  #to make this is in always uppercase


    def __str__():
        print(f"Name : {self.name} /nAmount : {self.amount} /n Payment Mode : {self.payment_type}")

class payment_tracker:
    def __init__(self):
        self.customers=[]
    def add__customers(self,customer):
        self.customers.append(customer)
    def calculate_payment(self):
        total_cash = 0
        total_card=

        