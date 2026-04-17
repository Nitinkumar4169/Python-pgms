#6. write a python pgm to calculate the factorial of a number
n = int(input("Enter the number: "))
def fact(n):
  if n<=1:
    return 1
  else:
    return n*fact(n-1)

#print("The factorial of {} = {}".format(n,fact(n)))
print(f"The factorial of {n} = {fact(n)}")