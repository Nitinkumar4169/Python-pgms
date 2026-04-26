#155.Write a python pgm to generate a random even number
import random
def is_even(n):
  if n<2:
    return False
  for i in range(2,n+1):
    if n%i==0:
      return True
  return False  

#function to genrate random even number
def generate_even_no(start,end):
  while True:
    num = random.randint(start,end)
    if is_even(num):
      return num
    
# Input range
start = int(input("Enter start: "))
end = int(input("Enter end: ")) 
print("Random even number: ",generate_even_no(start,end))    

