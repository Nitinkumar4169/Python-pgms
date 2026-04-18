#20. Write a python pgm to find first non-repeated character in a string
s = input("Enter the string: ")
ans = ""
for i in range(len(s)):
  if s.count(s[i]) == 1:
    print("First non repeated character is ",s[i])
    break
  

   

