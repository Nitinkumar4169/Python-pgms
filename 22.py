#22. Write a python pgm to find the smallest element in a list
lst = list(map(int, input("Enter the element in a list = ").split()))
#print(min(lst))

# Manual - way

min_ele = lst[0]
for i in range(1, len(lst)):
  if lst[i] < min_ele:
    min_ele = lst[i]

print("Smallest element in a list = ",min_ele)    
