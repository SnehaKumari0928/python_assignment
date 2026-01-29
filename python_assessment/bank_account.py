import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(asctime)s - %(levelname)s - %(message)s"
                    )


class InsufficientFundsError(Exception):
     pass
     
      
class InvalidAmountError(Exception):
     pass
     

class BankAccount:
     def __init__(self,account_number,initial_balance = 0):
          self.__account_number = account_number
          self.__balance = initial_balance
          self.__transactions = []

     def deposit(self, amount):
          if amount <= 0 :
                raise InvalidAmountError("Deposit amount must be positive")
          self.__balance += amount
              
          transaction = {"type":"deposit","amount":amount,"balance":self.__balance}
          self.__transactions.append(transaction)
          logging.info(transaction)
          
    
     def withdraw(self,amount):
            if self.__balance < amount:
              raise InsufficientFundsError("Insuffuicient balance")
            else:
              self.__balance -= amount
            transaction = {"type":"withdraw","amount":amount,"balance":self.__initial_balance}
            self.__transactions.append(transaction)
            logging.info(transaction)

     def get_balance(self):
          return f"Total balance in account is {self.__balance}"
     
     def get__transaction_history(self):
          return self.__transactions
     
     def __str__(self):
          return f"Account Number : {self.__account_number} | Balance : {self.__balance}"
     
               
               
account = BankAccount("8678845456566")

try:
     account.deposit(-999)
     account.withdraw(2000)

except InsufficientFundsError as e:
     print(f"Error:{e}")
except InvalidAmountError as e:
     print(f"Error:{e}")
account.deposit(1000)
print(account.get_balance())
print(account)
print(account.get__transaction_history())
     
          