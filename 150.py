#150.Write a python pgm to simulate rolling a dice
import random
def toss_coin(n):
  for i in range(n):
    result = random.choice(["Heads","Tails"])
    print(f"{i+1}: {result}")

n = int(input("Enter number of tosses: "))
toss_coin(n)