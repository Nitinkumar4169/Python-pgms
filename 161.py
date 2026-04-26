#161.Write a python pgm to check if a list is empty
lst = list(map(int,input("Enter the list elements: ").split()))
if len(lst)>=1:
  print("list is not empty")
else:
  print("list is empty")  