#100.Write a python to check if a key exist in a dictionary
d1 = {101:"Apple",201:"Ball",301:"cat",401:"Dog"}
key = int(input("Enter key to check: "))
if key in d1:
  print("key exists in dictionary")
else:
  print("Key doesn't exist in a dictionary")  
