#36.Write a python pgm to convert decimal into binary
def decimal_to_binary(num):
  binary = ""
  while num>0:
    rem = num%2
    binary += str(rem)
    num //= 2
     
  return binary[::-1]   

num = int(input("Enter the number = "))  
print(decimal_to_binary(num))