class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: {amount}, Updated Balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawn: {amount}, Remaining funds: {self.balance}')
        else:
            print('There is insufficient funds!')

acc = Account('Jake', 3000)
acc.deposit(1000)
acc.withdraw(750)
acc.withdraw(3300)
