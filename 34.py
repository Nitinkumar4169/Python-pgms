#34. Write a python pgm to find the GCD of a number

def GCD(a,b):
  while b!=0:
    a,b = b , a%b
    
  return a

a = int(input("Enter the 1st number = "))
b = int(input("Enter the 2nd number = "))

print("The gcd of two numbers is = ",GCD(a,b))

