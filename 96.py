#96.Write a py pgm to count frequency of characters in a string using dictionary
s = input("Enter the string: ")
freq = {}
for ch in s:
  if ch in freq:
    freq[ch] += 1
  else:
    freq[ch] = 1

print(freq) 
#or freq[ch] = freq.get(ch,0)+1        
    
  