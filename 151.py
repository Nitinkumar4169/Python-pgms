#151.Write a python pgm to simulate tossing a dice : multiple rolls
import random
def roll_dice(n):
  for i in range(n):
    result = random.randint(1,6)
    print(f"{i+1}: {result}")

n = int(input("Enter number of rolls: "))  
roll_dice(n)

