#Write a python pgm to find the longest word in a file
with open("1.py", 'r') as f:
  ans = f.read()

  words = ans.split()
  result = max(words, key=len)
print(result)