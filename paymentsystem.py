#write a python pan abstract class to design a payment system without methods like pay(), and implement it for UPI and card paymentsgm using 
from abc import *
#abstract class
class Payment(ABC):
  @abstractmethod
  def pay(self):
    pass

# UPI Payment class
class UPI(Payment):
  def pay(self):
    print("Payment done using UPI")

# CardPayment class
class CardPayment(Payment):
  def pay(self):
    print("Payment done using card")

upi = UPI()
cardpayment = CardPayment()
upi.pay()
cardpayment.pay()    

