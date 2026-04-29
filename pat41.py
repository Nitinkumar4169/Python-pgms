for i in range(1,6):
  for outerK in range(6-i-1):
    print(" ", end =" ")

  if i==1:
    print("1")
  else:
    print(i,end=" ")
    for innerK in range(2*i-3):
      print(" ",end=" ")  
    print(i)  