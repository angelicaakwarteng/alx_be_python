class BankAccount:
    def __init__(self, initial_balance):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount

    def display_balance(self):
        return f"Current Balance: $ {self.account_balance}"