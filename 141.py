#141.Write a python pgm to check if a number is divisible by another number
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1//num2:
  print(f"{num1} is divsible by {num2}")
else:
  print(f"{num1} is not divisible by {num2}")  