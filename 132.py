#132.Write a python pgm to check if a character is a special symbol
ch = input("Enter the string: ")
if not ch.isalnum():
  print("It is a special character")
else:
  print("It is not a special character")  