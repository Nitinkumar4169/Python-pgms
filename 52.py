#52. Write a python pgm to print all even numbers b/w 1 and 100 
def even_no():
  ans = []
  for i in range(1,101):
    if i%2 == 0:
      ans.append(i)
  return ans    
        
print("The even numbers b/w 1 and 100 = ",even_no())

#List comprehension
# ans = [i for i in range(1,101) if i%2 == 0]
# print(ans, end=" ")