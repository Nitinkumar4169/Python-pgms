#102.Write a python pgm to iterate over a list using 'while' loop
lst = list(map(int, input("Enter the list elements = ").split()))
i = 0
while i < len(lst):
  print(lst[i], end=" ")
  i += 1
  