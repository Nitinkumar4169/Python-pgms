#63.Wap to define a function that calculates fatorial using recursion
def fact(n):
  for i in range(1,n+1):
     if n<=1:
      return 1
  return n*fact(n-1)

n = int(input("Enter the number = "))  
print(fact(n))