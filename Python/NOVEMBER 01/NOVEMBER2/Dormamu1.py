# Problem 10: Payment System Using Polymorphism
# Logic: Base class Payment defines a general pay() method. Child classes override it.
# We can iterate through different payment objects and call pay() uniformly, relying on 
# python's dynamic method resolution (polymorphism) to execute the correct class method.
class Payment:
    def pay(self, amount):
        print("Processing generic payment.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ${amount}.")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing Credit/Debit Card payment of ${amount}.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Processing Cash payment of ${amount}.")

# Demonstrating polymorphism
payments = [UPIPayment(), CardPayment(), CashPayment()]
amount_to_pay = 150

for payment_method in payments:
    payment_method.pay(amount_to_pay)