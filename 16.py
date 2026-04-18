#16. Write a python pgm to count occurences of a substring in a string
string = input("Enter a string: ")
substring = input("Enter the substring: ")

count = 0
for i in range(len(string) - len(substring) + 1):
  if string[i:i+len(substring)] == substring:
    count += 1
print("Occurences of a substring in a string is: ", count)    
    

#  USING BUILT METHODS
# string = input("Enter a string:").lower()
# substring = input("Enter the substring:").lower()

# ans = string.count(substring)
# print(ans)