#67.Write a python pgm to define a function that checks if a string is palindrome
def is_palindrome(s):
  i = 0
  j = len(s)-1
  is_palindrome = True
  while i<j:
    if s[i]!=s[j]:
      return False
    else:
      i += 1
      j -= 1 
  return True     
     

s = input("Enter the string: ")  
print(is_palindrome(s))