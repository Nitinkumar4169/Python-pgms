#74.Write a python pgm to reverse a string using recursion
def reverse(s):
  if len(s) == 0:
    return s
  return reverse(s[1:])+s[:1]

s = input("Enter the string: ") 
print("The reversed string is: ",reverse(s)) 