class BankAccount:
    def __init__(self,balans:float):
        self.__balans = balans
        
    def deposit(self,deposit:float):
        self.deposit = deposit
        self.__balans += self.deposit
        
    def withdraw(self,withdraw:float):
        self.withdraw = withdraw
        self.__balans -= self.withdraw
        
    def get_balance(self):
        return f"{self._balans:,.2f}"
        
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())


    