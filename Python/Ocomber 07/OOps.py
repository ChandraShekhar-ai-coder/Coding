class Customer:
    def __init__(self,name,amount,payment_type):
        self.name = name
        self.amount = amount
        self.payment_type = payment_type.upper()  #to make this is in always uppercase

        customer1 = Customer("Salman",50000,"UPI")

    def Show Payment():
        print(f"Name : {self.name} \nAmount : {self.amount} \n Payment Mode : {self.payment_type}\n\n")

