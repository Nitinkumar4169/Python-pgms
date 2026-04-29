n = int(input("Enter the number: "))
for i in range(1,n+1):
  for outerK in range(n-i+1):
    print(" ",end = " ")

  
  if i == 1:
    print(chr(i+64))
  else:
    print(chr(i+64),end=" ")
    for innerK in range(2*i-3):
      print(" ",end = " ")  
    print(chr(i+64))  
