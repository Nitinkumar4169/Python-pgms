#136.Write a python pgm to count special special character in a string
s = input("Enter the string: ")
count = 0
for ch in s:
  if not ch.isalnum() and not ch.isspace():
    count += 1

print("Number of special characters in a string is: ",count)