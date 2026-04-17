#8. Write a python pgm to reverse a number
n = int(input("Enter the number: "))
#print(n[::-1]) #slicing method

#using while-loop

rev = 0
while n>0:
  lastdigit = n%10
  rev = rev*10 + lastdigit
  n = n//10

print("The reverse number is = ", rev)

