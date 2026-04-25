#133.Write a python pgm to count uppercase letters in a string
s = input("Enter the string: ")
count = 0
for ch in s:
  if ch.isupper():
    count += 1

  
print("Number of uppercase letters in a string is: ",count)      