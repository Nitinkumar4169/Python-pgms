#10. Write a python pgm to find the sum of digits of number
n = int(input("Enter the number: "))

sum=0
while n>0:
  digit = n%10
  sum = sum+digit
  n = n//10
  
print("Sum of digits of a number is = ",sum)  
  