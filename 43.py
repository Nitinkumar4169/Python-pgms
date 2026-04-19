#43.Write a python pgm to coutn words in a file
with open("1.py", 'r') as f:
  ans = f.read()
  words = ans.split()
  print("The number of words = ", len(words))

