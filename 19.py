#19. Write a python to check if two strings are anagram
string1 = input("Enter the string: ")
string2 = input("Enter the string: ")

ans1 = sorted(string1)
ans2 = sorted(string2)

if ans1 == ans2:
  print("strings are anagram")
else:
  print("Not an anagram")  

