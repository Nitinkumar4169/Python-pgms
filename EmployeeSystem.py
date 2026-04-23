#wap using an abstract class to design an Employee System, where different employees implement a salary() method

from abc import *

#Abstract class
class Employee(ABC):
  @abstractmethod
  def salary(self):
    pass

  
class FullTimeEmployee(Employee):
  def salary(self):
    return 50000
    
class ParTimeEmployee(Employee):
  def salary(self):
    hours = 5
    rate = 20000
    return hours*rate



#objects
pte =  ParTimeEmployee()
fte =  FullTimeEmployee()  

#calling
print("Full Time Salary:", fte.salary())
print("Part Time Salary:", pte.salary())


