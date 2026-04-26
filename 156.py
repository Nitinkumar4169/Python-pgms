#155.Write a python pgm to generate a random odd number
import random
def is_odd(n):
  if n<1:
    return False
  for i in range(1,n+1):
    if n%2!=0:
      return True
  return False  

#function to genrate random even number
def generate_odd_no(start,end):
  while True:
    num = random.randint(start,end)
    if is_odd(num):
      return num
    
# Input range
start = int(input("Enter start: "))
end = int(input("Enter end: ")) 
print("Random odd number: ",generate_odd_no(start,end))    

