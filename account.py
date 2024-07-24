class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw this amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit this amount")
        self.balance += amount

    def transfer(self, receiver:'Account', amount):
        if amount <= 0:
            raise ValueError("Cannot transfer this amount")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        receiver.balance += amount