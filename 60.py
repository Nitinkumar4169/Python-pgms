#60.Write a python pgm to print numbers divisible by 3 and 5 up to 100
ans = [i for i in range(3,101) if i%3==0 or i%5==0]
print(ans)
