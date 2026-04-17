#write a python to remove all spaces from a string
s = input("Enter the string: ")
def remove_spaces(s):
  result = " "
  for char in s:
    if char != " ":
      result += char
  return result

print(remove_spaces(s))