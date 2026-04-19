#31. Write a python pgm to check if a number is an Armstrong or not
#ARMSTRONG NUMBER = 371 = 3^3 + 7^3 + 1^3 => 371

def armstrong_number(num):
  dup = num
  sum = 0
  while num>0:
    digit = num%10
    sum += pow(digit,3)
    num = num//10

  return dup == sum 

num = int(input("Enter the numbers: "))  

if armstrong_number(num):
  print("It's an armstrong number")
else:
  print("Not an armstrong number")  
  

  