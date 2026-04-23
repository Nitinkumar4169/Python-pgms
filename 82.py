#82.Write a python pgm to find the minimum element in a tuple
ans = tuple(map(int, input("Enter the elements: ").split()))
#print(min(ans))

#or
min_val = ans[0]
for i in ans:
  if i < min_val:
    min_val = i

print(min_val)