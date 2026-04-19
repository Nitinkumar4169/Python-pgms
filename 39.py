#39.Write a python pgm to find the sum of natural numbers up to 'n'
def sum_s(n):
  sum = 0
  for i in range(0,n):
    sum += i
  return sum  

n = int(input("Enter the natural: "))  
print("Sum of natural numbers up to n =",sum_s(n))