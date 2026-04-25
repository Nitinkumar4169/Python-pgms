#149.Write a python pgm to pick a random element from a list
import random
lst = list(map(int, input("Enter the list elements: ").split()))
ans = random.choice(lst)
print("The random pick element from a list is: ", ans)