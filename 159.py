#158.Write a python pgm to generate random floating-point numbers
import random

for i in range(5):
  num = random.uniform(0,100)
  print(f"Float {i+1}: {round(num, 2)}")
