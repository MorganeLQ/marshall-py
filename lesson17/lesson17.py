#lesson 17

# input
num = int(input("Enter a number: "))

total_product = 1

for i in range(num, 0, -1): #or range(1, num+1)
    #range(a, b, steo) --> if step not provided, it is assumed to be 1
    #i represents each value in sequence
    total_product *= i
print(f"Factorial of {num} is {total_product}.")
