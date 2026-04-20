#54. Write a python pgm to calculate the sum of 'n' natural nubers using a loop
def sum_n(n):
  sum = 0
  for i in range(n):
    sum = sum +i

  return sum  
n = int(input("Enter the number = "))  
print(f"The sum of {n} natural number is:", sum_n(n))


