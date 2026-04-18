#21. Write a python pgm to find the largest element in a list
# my_list = list(input("Enter the list elements: "))
# print(my_list)

# print(max(my_list))

# MANUAL - WAY
lst = list(map(int, input("Enter the list elements: ").split()))

max_val = lst[0]

for i in range(1,len(lst)):
  if lst[i] > max_val:
    max_val = lst[i]

print("Largest element in a list: ", max_val)    

