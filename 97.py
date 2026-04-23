#97.Write a py pgm to count frequency of words in a string using dictionary
s = input("Enter the string: ")
freq = {}
words = s.split()
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1  

print(freq)

#OR
#for word in s.split():
 #   freq[word] = freq.get(word, 0) + 1