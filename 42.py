#42. Write a python pgm to write to a text file
f = open("1.py",'a')
ans = f.write("Hello this is new content\n")
print(ans)
f.close()