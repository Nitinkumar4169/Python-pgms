#62.Write a python pgm to define a function that checks if a number is prime
def check_prime(n):
  if n<=1:
    print("Not an prime number")
   
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      print("Not an prime number") 

  return " This is a prime number"  
    
n = int(input("Enter the number: "))   
print(check_prime(n))



