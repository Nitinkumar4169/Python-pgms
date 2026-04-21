#65.Write a python pgm to define a function that returns the reverse of a string
def reverse_string(s):
  if len(s) == 0:
    return s
  return reverse_string(s[1:])+s[0]
 
s = input("Enter the string: ")
print("The reversed string is = ", reverse_string(s))
