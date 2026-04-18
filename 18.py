#Write a python pgm to replace vowels with '*';
s = input("Enter the string: ")

ans = ""
for i in range(len(s)):
  if s[i] in "aeiouAEIOU":
    ans = ans + '*'
  else:
    ans += s[i]

print(ans)    
      
 