#29.Write a python pgm to find common elements b/w two lists.
lst1 = input("Enter the  1st list elements = ").split()
lst2 = input("Enter the 2nd list elements = ").split()
common = []
for i in lst1:
    if i in lst2:
      common.append(i)

print("Common elements are: ",common)  
#common = list(set(lst1) & set(lst2))    