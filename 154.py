#154.Write a python pgm to generate a random prime number
import random

def is_prime(n):
  if n<2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n%i == 0:
      return False
    return True

#function to generate random prime nummber
def generate_prime(start,end):
  while True:
    num = random.randint(start,end)
    if is_prime(num):
      return num
    
# Input range
start = int(input("Enter start: "))
end = int(input("Enter end: "))  
print("Random prime number: ",generate_prime(start,end))



  