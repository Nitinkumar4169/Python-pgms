#76.Write a python pgm to find GCD of two numbers using recursion
def GCD(a,b):
  if b==0:
    return a
  return GCD(b,a%b)

a = int(input("Enter the 1st number = "))
b = int(input("Enter the 2nd number = "))  
print("The gcd of two numbers is = ",GCD(a,b))