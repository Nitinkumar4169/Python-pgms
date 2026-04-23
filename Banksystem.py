#wap using an abstract class to represent a Bank System, where each bank implements an interest_rate() method

from abc import *
# Bank class
class Bank(ABC):
  @abstractmethod
  def interest_rate(self):
    pass

#SWISS BANK
class SWISS(Bank):
  def interest_rate(self):
    return 5
  
class Deustche(Bank):
  def interest_rate(self):
    return 6

#objects
d = Deustche()
s = SWISS()

print("The interest rate of Deusctche bank is: ", d.interest_rate(),"%")
print("The interest rate of SWISS bank is: ", s.interest_rate(),"%")
