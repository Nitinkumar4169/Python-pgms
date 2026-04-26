#157.Write a python pgm to generate a random string of given length
import random
import string

def generate_string(length):
  #Here, we can take letters only
  characters = string.ascii_letters #+ string.digits + string.punctuation
  return "".join(random.choice(characters) for _ in range(length))

length = int(input("Enter length: "))
print("Random string: ",generate_string(length))