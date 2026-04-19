#40.Write a python pgm to calculate the power of a number without using '**'
def calc_power(base,exponent):
  ans = 1
  for i in range(exponent):
    ans *= base 
  return ans  
        
base = int(input("Enter the base = "))  
exponent = int(input("Enter the exponent = "))
print(calc_power(base,exponent))