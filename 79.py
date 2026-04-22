#79.Write a python pgm to find the length of a string using recursion
def len_string(s):
  if s == "":
    return 0
  return 1 + len_string(s[1:])

s = input("Enter the string = ") 
print("The length of a string is: ",len_string(s)) 