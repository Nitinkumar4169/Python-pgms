#148.Write a python pgm to shuffle element of a list
import random
lst = list(map(int,input("Enter the list elements: ").split()))
random.shuffle(lst)
print("The shuffle element in a list is: ", lst)

