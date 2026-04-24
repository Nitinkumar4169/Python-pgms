#101.Write a python pgm to iterate over a list using 'for' loop
lst = list(map(int, input("Enter the list elements = ").split()))
for i in lst:
  print(i, end="")
