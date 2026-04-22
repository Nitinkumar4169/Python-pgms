#71Write a python pgm to calculate factorial using recursion
def factorial(n):
  if n<=1:
    return 1
  else:
    return n*factorial(n-1) 

n = int(input("Enter the number = "))  
print(f"The factorial of a {n} = ", factorial(n))