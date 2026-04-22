#78.Write a python pgm to calculate sum of digits using recursion
def sumofdigits(n):
  if n<=1:
    return n
  return n+sumofdigits(n-1)

n = int(input("Enter the number = "))
print("The sum of digits = ", sumofdigits(n))  