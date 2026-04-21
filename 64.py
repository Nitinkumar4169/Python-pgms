#64.Write a python pgm to define a function that finds the maximum of three numbers
def maximum(a,b,c):
  if a>b and a>c:
    return f"a = {a}"
  elif b>a and b>c:
    return f"b = {b}"
  else:
    return f"c = {c}"

a = int(input("Enter the 1st number = "))  
b = int(input("Enter the 2nd number = "))
c = int(input("Enter the 3rd number = "))  
print("The nmaximum no. b/w three numbers is: ",maximum(a,b,c))