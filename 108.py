#108.Write a python pgm to find the smallest word in a sentence
lst = list(input("Enter the sentence: ").split())
smallest = lst[0]
for i in lst:
  if len(i) < len(smallest):
     smallest = i
print("The smallest word in a sentence is: ",smallest)