#25. Write a python pgm to sort a list in ascending order
lst = list(map(int, (input("Enter the no. of list: ").split())))
# ans = sorted(lst)
# print(ans)

for i in range(len(lst)):
  for j in range(i+1, len(lst)):
    if lst[i] > lst[j]:
      lst[i], lst[j] = lst[j], lst[i]

print(lst)      

