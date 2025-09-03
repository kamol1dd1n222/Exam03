from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount:float):
        self.amount = amount
        return self.amount
        
    
class PayPalPayment(Payment):
    def pay(self,amount):
        self.amount = amount
        return f"Paid {self.amount} using PayPal"
    
    
class CardPayment(Payment):
    def pay(self,amount):
        self.amount = amount
        return f"Paid {self.amount} using Card"
    
p1 = PayPalPayment()
p2 = CardPayment()
print(p1.pay(100))
print(p2.pay(200))