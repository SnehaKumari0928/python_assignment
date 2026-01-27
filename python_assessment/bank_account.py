import logging

logging.basicConfig(level="INFO")


class InsufficientFundsError(Exception):
     def __init__(self):
          return None
      
class InvalidAmountError(Exception):
     def __init__(self):
          return None
     

class BankAccount:
     transactions = []
     def __init__(self,account_number,initial_balance = 0):
          self.__account_number = account_number
          self.__initial_balance = initial_balance

     def deposit(self, amount):
          if type(amount) != int :
                raise InvalidAmountError
          self.__initial_balance += amount
              

          BankAccount.transactions.append({"type":"deposit","amount":amount,"balance":self.__initial_balance})
    
     def withdraw(self,amount):
            if self.__initial_balance < amount:
              raise InsufficientFundsError
            else:
              self.__initial_balance -= amount
            BankAccount.transactions.append({"type":"withdraw","amount":amount,"balance":self.__initial_balance})

     def get_balance(self):
          return f"Total balance in account is {self.__initial_balance}"
     
     def get__transaction_history(self):
          return BankAccount.transactions
     
     def __str__(self):
          return f"Account Number : {self.__account_number}, Balance : {self.__initial_balance}"
     
     def log_transaction(self):
          logging.info(BankAccount.transactions)
               
               
a1 = BankAccount("8678845456566")

try:
     a1.deposit("900")
     a1.withdraw(2000)

except InsufficientFundsError as e:
     print(f"Error:{e} Insufficient balance")
except InvalidAmountError as e:
     print(f"Error:{e} Please enter valid amount")
a1.deposit(1000)
print(a1.get_balance())
a1.log_transaction()

print(a1.get__transaction_history())
     
          