#30 Write a python pgm to rotate a list by 'k' positions.

def rotate_left(lst,k):
  k = k%len(lst)
  return lst[k:] + lst[:k]

lst = list(map(int, input("Enter the list elements: ").split()))
k = int(input("Enter k: "))
print(rotate_left(lst,k))


