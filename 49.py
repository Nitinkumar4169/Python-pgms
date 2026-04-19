#Write a python pgm to remove blank lines from a file
with open("1.py", 'r') as f:
  lines = f.readlines()

with open("1.py",'w') as f:
  for line in lines:
    if line.strip() != "":
      f.write(line)
