#164.Wap to check if a dictionary is empty
d = {}
n = int(input("Enter number of items: "))
for i in range(n):
  key = input("Enter keys: ")
  value = input("Enter values: ")
  d[key] = value

if not d:
  print("dictionay is empty")  
else:
  print("dictionary is not empty")  