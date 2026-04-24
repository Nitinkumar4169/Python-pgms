#104.Write a python pgm to check if an element exist in a tuple
tple = tuple(map(int, input("Enter the element in a tuple = ").split()))
ele = int(input("Enter the element to check = "))

if ele in tple:
   print("Element exist in a tuple")
else:
  print("Element does not exist in a tuple")   


