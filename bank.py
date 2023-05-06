class Bank:
    bank_name="Equity"
    def __init__(self,account_name,account_number,balance):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
            self.balance+=amount
             
            return(f"I now have {self.balance} in my account")
    def withdraw(self,amount):
         if self.balance <= amount:
              return(f"You have insufficient amount")
         else: 
             self.balance-=amount
             return (f"You have {self.balance} remaining")
    def current_amount(self):
         return(f"Your current balance stands at {self.balance}")

             


Esther=Bank(account_name="Esther",account_number="54678A",balance=50000)
print(Esther.deposit(10000))
print(Esther.withdraw(20000))
print(Esther.current_amount())

