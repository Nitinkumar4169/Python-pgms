#103.Write a python pgm to find the sum of elements in a tuple
tple = tuple(map(int, input("Enter the elements in a tuple = ").split()))
sum = 0
for i in tple:
  sum += i
print("Sum of elements in a tuple is: ",sum)
