class BankAccount: 

#testing multiple repos in VS Code

    bank_name = "MyBank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}."
        elif amount == 0:
            return "Deposit amount must be greater than zero."
        elif amount < 0:
            return "Deposit amount cannot be negative."
        

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}."
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be greater than zero."

    def get_balance(self):
        return self.balance


account_1 = BankAccount("Alice", 1000)

print(account_1.bank_name)  # Accessing class attribute


account_2 = BankAccount("Bob", 500)

account_2.bank_name = "YourBank"  # Modifying class attribute through an instance

print(f"Bank name for {account_2.owner}: {account_2.bank_name}")

print(account_1.deposit(200)) 

print(account_1.get_balance())   # should be 1200 after deposit
print(account_2.get_balance())   # should still be 500 — untouched