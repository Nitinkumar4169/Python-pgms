#77.Write a python pgm to find the LCM of two numbers using recursion
def GCD(a,b):
  if b==0:
    return a
  return GCD(b,a%b)

def lcm(a,b):
  return a*b // GCD(a,b)


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))  
print("The LCM of two numbers is: ", lcm(a,b))