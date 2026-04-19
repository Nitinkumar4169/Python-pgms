#35. Write a python pgm to find the LCM of two numbers.
def is_lcm(a,b):
  i = 2
  lcm = 1
  while a>1 or b>1:
    if a%i == 0 or b%i == 0:
      if a%i == 0:
        a //= i
      if b%i == 0:  
       b //= i
      lcm *= i
    else:
      i += 1  
  return lcm    

a = int(input("Enter the 1st number = "))  
b = int(input("Enter the 2nd number = "))
print("The LCM of two numbers is: ", is_lcm(a,b))

#using formual direct
# def GCD(a,b):
#   while b!=0:
#     a,b = b , a%b
    
#   return a

# a = int(input("Enter the 1st number = "))
# b = int(input("Enter the 2nd number = "))

# def lcm(a,b):
#   return a*b//GCD(a,b)
# print(lcm(a,b))