# Problem 6: Bank Account Management
# Logic: Maintain balance as an instance variable.
# deposit() adds to balance. withdraw() checks if amount <= balance before subtracting.
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Failed to withdraw ${amount}. Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Current Balance: ${self.balance}")
        print("-" * 20)

# Creating an object and testing methods
account = BankAccount("Jane Smith", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)  # Should trigger insufficient funds
account.display_balance()