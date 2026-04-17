#11. Write a python pgm to reverse a string
n = input("Enter the string: ")
#print(n[::-1])

rev = ""
for i in n:
  rev = i + rev

print(rev)  