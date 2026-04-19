#Write a python pgm to count lines in a file
with open("1.py", 'r') as f:
  count = 0
  for lines in f:
    count += 1
  print("The number of lines = ", count)  