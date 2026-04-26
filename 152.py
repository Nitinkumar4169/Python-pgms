#152.Write a python pgm to generate a random password
import random
import string

def generate_strong_password(length):
  if length < 4:
    print("Password length should be at least 4")

    #Ensure one of each
  password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
  ]
  
   # All possible characters
  characters = string.ascii_uppercase + string.digits + string.punctuation
  password += [random.choice(characters) for _ in range(length - 4)]
    
  random.shuffle(password)
   # Convert list to string
  return "".join(password)

length = int(input("Enter password length: "))  
print("Strong Password: ",generate_strong_password(length))