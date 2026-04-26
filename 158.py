#158.Write a python pgm to generate random alphanumeric string
import random
import string

def generate_alphanumeric(length):
  characters = string.ascii_letters +string.digits
  return "".join(random.choice(characters) for _ in range(length))

length = int(input("Enter length:"))
print("The alphanumeric string is: ",generate_alphanumeric(length))