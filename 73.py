#73.Write a python pgm to find the sum of natural number using recursion
def sum_natural(n):
  if n==0:
    return 0
  return n + sum_natural(n-1)

n = int(input("Enter the number = ")) 
print(f"The sum of natural number {n} is: ",sum_natural(n)) 