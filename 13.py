#13. Write  a python pgm to count vowels and consonants in a string

s = input("Enter the string: ")
def count_vowels_consonants(s):
  vowels = 0
  consonants = 0
  for char in s:
    if char.lower() in 'aeiou':
      vowels += 1
    elif char.isalpha():
      consonants += 1
  return vowels, consonants  
  
vowels, consonants = count_vowels_consonants(s)
print("Number of vowels: ", vowels)
print("Number of consonants: ", consonants)
