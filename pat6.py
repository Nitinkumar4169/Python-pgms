
for i in range(1,5):
  for outerK in range(5-i+1):
    print(" ",end = " ")

  
  if i == 1:
    print(chr(i+64))
  else:
    print(chr(i+64),end=" ")
    for innerK in range(2*i-3):
      print(" ",end = " ")  
    print(chr(i+64))  

   
for i in range(1,5+1):
  for outerK in range(i):
    print(" ",end = " ")

  
  if i == 5:
    print(chr(65))
  else:
    print(chr(70-i),end=" ")
    for innerK in range(2*(5-i)-1):
      print(" ",end = " ")  
    print(chr(70-i))  

