#45.Write a python pgm to copy contents from one file to another
with open("1.py" ,'r') as f1:
  ans1 = f1.read()

with open("2.py", 'w') as f2:
  ans2 = f2.write(ans1)

print("The 1.py file has been copied to 2.py file",ans2)  
    