class BankAccount:
    def __init__(self,amount ,account_balance = 0):
       self.account_balance = account_balance
       self.amount = amount
    def deposit(self):
         return  self.account_balance + self.amount
    def withdraw(self):
          return  self.account_balance - self.amount
    def display_balance(self):
          pass   

userOne = BankAccount(0,0)
print (userOne.withdraw())
