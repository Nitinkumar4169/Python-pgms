n = int(input("Enter the number: "))
for i in range(1,n+1):
  for outerK in range(i):
    print(" ",end = " ")

  
  if i == n:
    print(i)
  else:
    print(i,end=" ")
    for innerK in range(2*(5-i)-1):
      print(" ",end = " ")  
    print(i)  
