#75.Write a python pgm to check if a string is palindrome using recursion
def is_palindrome(s):
  if len(s) <= 1:
    return True
  if s[0]!=s[-1]:
    return False
  return is_palindrome(s[1:-1])

s = input("Enter the string: ")
print("The string is palindrome: ", is_palindrome(s))