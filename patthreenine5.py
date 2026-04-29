#n = int(input("Enter the number: "))

for i in range(1,5):
  for outerK in range(5-i-1):
    print(" ", end =" ")

  if i==1:
    print("1")
  else:
    print(i,end=" ")
    for innerK in range(2*i-3):
      print(" ",end=" ")  
    print(i)  



for i in range(1,6):
  for outerK in range(i):
    print(" ",end = " ")

  
  if i == 5:
    print(i,end=" ")
  else:
    print(i,end=" ")
    for innerK in range(2*(5-i)-1):
      print(" ",end = " ")  
    print(i)  
