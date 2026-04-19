#46. Write python pgm to check if a file exists
import os

if os.path.isfile("1.py"):
  print("File exist")
else:
  print("File doesn't exist")  