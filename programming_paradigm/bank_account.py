class BankAccount:
    def __init__(self, initial_balance):
        self.account_balance = initial_balance

    def deposit(self, amount):
        BankAccount = 0
        BankAccount = self.account_balance + amount
        return BankAccount

    def withdraw(self, amount):
        if amount < self.account_balance:
            BankAccount = self.account_balance - amount
        return f"Withdrew: {amount}. Your new balance is {BankAccount}"

    def display_balance(self):
        return f"Current Balance: $ {self.account_balance}"