#Write python pgm to find the second largest element in a list
lst = list(map(int, input("Enter the list: ").split()))


def secondlargest(lst):
  largest =  lst[0]
  slargest =  float('-inf')
  for i in lst:
    if i > largest:
      slargest = largest
      largest = i
    elif i < largest and i > slargest:
      slargest = i
  return slargest    
print("second largest elment =",secondlargest(lst))    



 