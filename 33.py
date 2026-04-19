#Write a python pgm to check if a number is a palindrome
def is_palindrome(n):

  reversed = 0
  original = n
  while n>0:
    digit = n%10
    reversed = reversed*10 + digit
    n = n//10
  return original == reversed  

n = int(input("Enter the number = ")) 

if is_palindrome(n):
  print("This is a palindrome number")
else:
  print("This is not an palindrome number")  