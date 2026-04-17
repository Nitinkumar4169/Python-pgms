#9. write a python pgm to check if a number is prime
n = int(input("Enter the number: "))
flag = 0
i=2
while i*i<=n:
  if n%i == 0:
    flag = 1 
    break
  i = i+1  

if n<=1:
  print("This is not a prime number")
elif flag==0:
  print("This is a prime number")
else:
  print("Not a prime number")  
  