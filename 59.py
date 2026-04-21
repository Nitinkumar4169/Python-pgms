#59.Write a python pgm to print prime numbers b/w 1 and 100
num = 2
for num in range(2,101):
  is_prime = True

  for i in range(2, int(num**0.5) + 1):
    if num%2 == 0:
      is_prime = False
      break

  if is_prime:
    print(num, end =" ")  

      