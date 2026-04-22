#68.Write a python pgm to define a function that returns sum of digits of a number
def sum_digits(n):
  sum = 0
  while n>0:
    digit = n%10
    sum += digit
    n = n//10
  return sum  
   
n = int(input("Enter the number = "))  
print("The sum of digits of a number is: ", sum_digits(n))