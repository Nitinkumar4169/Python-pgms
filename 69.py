#69.Write a python pgm to define a function that generates Fibonacci series up to 'n'
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number = ")) 
print(f"The Fibonacci series of {n} is: ", end="")
Fibonacci(n)