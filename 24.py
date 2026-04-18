#24.Write a python pgm to remove duplicate from a list
lst = list(map(int, input("Enter the list: ").split()))
# duplicates = []
# for i in range(0,len(lst)):
#  if lst.count(i) >= 1 and i not in duplicates:
#   duplicates.append(i)

# print(duplicates)  

#OR 
# unique = list(set(lst))
# print(unique)

# Using Dictionary
freq = {}
duplicates = []
for i in lst:
 if freq[i] = freq.get(i,0)+1

for key in freq:
 if freq[key] > 1:
  duplicates.append(key)

print(duplicates)  
 
