#160.Write a python pgm to generate random numbers within a range.
import random

a = int(input("Enter the a: ")) 
b = int(input("Enter the b: ")) 

for i in range(a,b):
  ans = random.randint(a,b)
  print(ans)
