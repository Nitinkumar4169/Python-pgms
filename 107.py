#107.Write a python pgm to find the largest word in a sentence
lst = list(input("Enter the sentence: ").split())
largest = ""
for i in lst:
  if len(i) > len(largest):
     largest = i
print("The largest word in a sentence is: ",largest)