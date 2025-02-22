from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def get_account(self):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass

class RealBankAccount(BankAccount):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
            print(f"An amount has been withdrawn and the balance is {self.balance}")
        else:
            print("insufficient balance. Deposit enough money to withdraw")

    def get_account(self):
        print( f"the balance in the account is {self.balance}")
    
class ATMProxy(BankAccount):

    def __init__(self, bank_account):
        self.bank_account =bank_account
        self.authentication = False

    def authenticate(self, pin):
        if pin == "1234":
            self.authentication = True
            print("Authentication successful")
        else:
            print("Autherntication failed")

    def withdraw(self, amount):
        if not self.authentication:
            print("Please authenticate first")
            return False
        self.bank_account.withdraw(amount)
    

    
    def get_account(self):
        if not self.authentication:
            print("Please authenticate first")
            return False
        self.bank_account.get_account()


real_bank_account = RealBankAccount("savings",1000)
atm_proxy = ATMProxy(real_bank_account)
atm_proxy.withdraw(100)
atm_proxy.authenticate("0000")
atm_proxy.authenticate("1234")
atm_proxy.withdraw(100)
atm_proxy.get_account()
