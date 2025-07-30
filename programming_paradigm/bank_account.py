class BankAccount:
    def __init__(self, initial_balance):
        self.account_balance = initial_balance

    def deposit(self, amount):
        BankAccount = 0
        self.account_balance += amount
        return BankAccount.append(self.account_balance)

    def withdraw(self, amount):
        self.account_balance -= amount

    def display_balance(self):
        return f"Current Balance: $ {self.account_balance}"