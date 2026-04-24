#112.Write a python pgm to calculate simple interest
p = int(input("Principal (initial amount): "))
r = int(input("Rate of interest (per year): "))
t = int(input("Time (in years): "))

SI = p*r*t//100
print("Simple Interest is: ",SI)