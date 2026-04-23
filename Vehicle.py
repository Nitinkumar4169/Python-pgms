#Wap to design an abstract class to design a Vehicle System with a method start(), and implement it Car and Bike

from abc import *

#abstract class
class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

# Car class
class Car(Vehicle):
  def start(self):
    print("The car has started")

# Bike class
class Bike(Vehicle):
  def start(self):
    print("The bike vehicle has started")  

#objects
b = Bike()
c = Car()

b.start()
c.start()

