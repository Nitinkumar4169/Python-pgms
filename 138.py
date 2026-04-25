#138.Write a python pgm to replaces spaces with hyphens in a string
import string
s = input("Enter the string: ")
ans = ""
for ch in s:
  if ch.isspace():
    ans +=  "-"
  else:
    ans += ch  
print("The spaces has been replaced with hyphens: ", ans)    

