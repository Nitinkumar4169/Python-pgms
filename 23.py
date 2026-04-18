#23. Write a python to calculate the sum of elements in a list
lst = list(map(int, input("Enter the elements in a list = ").split()))
sum = 0
for i in range(0, len(lst)):
  sum += lst[i]

print(sum)  
