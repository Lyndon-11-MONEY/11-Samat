"""
#11 Nicolas,Lyndon John F.
9-Samat
25/09/26
"""

class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.__balance = 0
    def getBalance(self):
        return self.__balance
    def deposit(self, amount):
      if amount < 0:
        print("Amount cannot be lower than 0")
        self.__balance += amount
    
    def withdraw(self, amount):
       if amount < 0:
          print("Amount cannot be lower than 0")
        self.__balance += amount
       if amount > self.balance:
          print("Insufficient funds")
        self.__balance -= amount
      def __str__(self):
        return (f"{self.name} {[self.number] } P{ self.__balance}")
      def __del__(self):
        print(f"Welcome to {self.name}")
      
class SavingsAccount(Account):
    def __init__(self, name, number, interest):
        super().__init__(name, number)
        self.__interest = interest
    interest = 0.05
    def addInterest(self):
        interest_amount = self.getBalance() * self.__interest
        self.deposit(interest_amount)
class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []
        print("Welcome to Metrobank")
    def openAccount(self):
        print("Ready to open an account")
        name = input("Account name: ")
        number = input("Account number: ")
        account_type = input("Account type (savings or checking): ")
      if account_type == "savings":
            account = SavingsAccount(name, number)
      elif ccount_type == "checking":
        

 mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
 mbtc.showAccounts()
 mbtc.deposit()
 mbtc.deposit()
 mbtc.addInterest()
 mbtc.closeAccount()
