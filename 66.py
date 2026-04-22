#66.Write a python pgm to define a function that count vowels in a string
def count_vowels(s):
  count = 0
  for ch in s:
    if ch in "aeiouAEIOU":
      count += 1    
  return count    

s = input("Enter the string: ")  
print("The number of vowels in a string is: ",count_vowels(s))
