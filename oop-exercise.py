class BankAccount:
    def __init__ (self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough funds"
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def display(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

myAccount = BankAccount("Azijur Rahaman", 1000)
print(myAccount.display())
myAccount.deposit(500)
print(myAccount.display())
myAccount.withdraw(600)
print(myAccount.display())
print(myAccount.get_balance())