#53.Write a python pgm to print all odd numbers b/w 1 and 100
# def odd_no():
#   ans = []
#   for i in range(1,101):
#     if i%2 == 1:
#       ans.append(i)
#   return ans
# print("The odd numbers b/w 1 and 100 = ", odd_no())

ans = [i for i in range(1,101) if i%2 == 1]
print(ans)

    