#37. Write a python pgm to convert binary into decimal
def binary_to_decimal(b):
    n = len(b)
    ans = 0
    for i in range(0,n):
      if b[n-i-1] == '1':
         ans += 2**i
    return ans    


b = input("Enter the binary number: ")
print(binary_to_decimal(b))