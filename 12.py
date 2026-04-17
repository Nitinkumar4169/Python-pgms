#12. Write a python pgm to check if a string is a palindrome or not
s = input("Enter a string: ")
def is_palindrome(s):
  left = 0
  right = len(s)-1
  while left<right:
    if s[left] != s[right]:
      return False
    left += 1
    right -=1
  return True  

if is_palindrome(s):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")