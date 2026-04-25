#140.Write a python pgm to join words into a sentence
s = input("Enter the string: ")
word = s.split()
result = " ".join(word)
print("The sentence is: ", result)