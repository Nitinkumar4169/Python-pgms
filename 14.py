#14. write a python pgm to find the length of a string without using 'len()' function
s= input('Enter a string: ')
def string_length(s):
  count = 0
  for char in s:
    count += 1
  return count

Length = string_length(s)
print("The length of the string is: ", Length)
  
