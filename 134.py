#134.Write a python pgm to count lowercase letters in a string
s = input("Enter the string: ")
count = 0
for ch in s:
  if ch.islower():
    count += 1

  
print("Number of lowercase letters in a string is: ",count)      