#72.Write a python pgm to generate Fibonacci series using recursion
def fibo(n):
  if n==1 or n==0:
    return n
  else:
    return fibo(n-1)+fibo(n-2)

n = int(input("Enter the number = ")) 
for i in range(n):
  print(fibo(i), end=" ") 