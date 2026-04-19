#Write a python pgm to check if a number is a perfect number
#A Perfect Number is a number that is equal to the sum of its proper
# divisors 
#(excluding the number itself).
def is_perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum += i 

  return sum == n    
     
n = int(input("Enter the number = "))  
print(is_perfect(n))

if is_perfect(n):
  print("Number is s perfect number")
else:
  print("Not an perfect number")   
