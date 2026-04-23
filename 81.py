#81.Write a python pgm to find the maximum elements in a tuple
ans = tuple(map(int, input("Enter the elements: ").split()))
#print(max(ans))

#or
max_val = ans[0]
for i in ans:
  if i > max_val:
    max_val = i

print(max_val)    
