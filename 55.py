#55.Write a python pgm to print a pyramid pattern of stars
def pyramid_pattern(n):
  for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
   
n = int(input("Enter the number: "))
print(pyramid_pattern(n))
