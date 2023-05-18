
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else: 
            print('Sorry. Not enough money')
    
    def statement(self):
        print(f'Account Balance ${self.balance}')

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance= -1000)

    def __str__(self):
        return f"{self.name}'s Current Account: Balance ${self.balance}"

class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance, min_balance= 0)

    def __str__(self):    
        return f"{self.name}'s Savings Account: Balance ${self.balance}"


x = Current('Arik', 222)
x.withdraw(10000)
print(x)