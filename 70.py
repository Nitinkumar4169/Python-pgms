#70.Write a python pgm to define a function that calculates power of a number using recursion
def calc_power(base,exp):
  if exp == 0:
    return 1
  return base*calc_power(base,exp-1) 

base = int(input("Enter the base: "))  
exp = int(input("Enter the exp: "))  
print("The power of a number is: ", calc_power(base,exp))