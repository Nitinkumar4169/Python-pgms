#28. Write a python pgm to merge two list
lst1 = input("Enter the  1st list elements = ").split()
lst2 = input("Enter the 2nd list elements = ").split()

ans = lst1 + lst2
print("Merge list is: ", ans)

# or we can use extend here
#lst1.extend(lst2)
#print(lst1)~