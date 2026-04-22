#80.Write a python pgm to print numbers from 'n' to 1 using recursion
def print_nos(n):
  if n==0:
    return 
  print(n,end=" ")
  print_nos(n-1)
   
n = int(input("Enter the number = "))
print(f"The numbers from {n} to 1 is: ", end="")  
print_nos(n)