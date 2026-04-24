#109.write a python pgm to count the number of words in a sentence
s = input("Enter the sentence: ").split()
count = 0
for i in s:
  count += 1

print("Number of words in a sentence is: ",count)  
