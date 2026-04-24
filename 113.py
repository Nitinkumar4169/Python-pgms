#113.Write a python pgm to calculate compound interest
p = int(input("Principal: "))
r = int(input("Rate of interest (per year): "))
t = int(input("Time (in years): "))
CI = p * (1 + r/100) ** t - p

print("The compound interest is: ",round(CI,2))