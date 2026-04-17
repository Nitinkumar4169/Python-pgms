#7. Write a python pgm to generate the Fibonacci series
n = int(input("Enter the number: "))
def fibo(n):
  if n==0 or n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

print(f"The fibonacci number of {n} = {fibo(n)}")    