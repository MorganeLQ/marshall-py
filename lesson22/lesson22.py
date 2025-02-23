#lesson 22

#input
upper_limit = int(input("Enter N to find the Nth Fibonacci number: "))

#initialize variables
fib_0 = 0
fib_1 = 1
fib_n = 0 #n is currently 2

for n in range(2, upper_limit+1):
    fib_n = fib_1 + fib_0 #calculate fib(n)
    
    #next fib(n)
    fib_0 = fib_1
    fib_1 = fib_n
    
print(f"Fibonacci({upper_limit}) is {fib_n}.")
