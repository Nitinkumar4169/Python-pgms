#135.Write a python pgm to count digits in a string
s = input("Enter the string: ")
count = 0
for ch in s:
  if ch.isdigit():
    count += 1

print("Number of digits in a string is: ",count)  