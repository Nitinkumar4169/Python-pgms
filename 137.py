#137.Write a python pgm to remove punctuation from a string
import string
s = input("Enter the string: ")
ans = ""
for ch in s:
  if ch not in string.punctuation:
    ans += ch
  
print("Punctuation is removed from a string: ",ans)