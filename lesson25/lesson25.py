#lesson 25

#input
num = int(input("Enter a value:"))
num_copy = num

#initialize variable
largest = 0

while num % 2 == 0:
    #is num divisible by 2 and keep dividing by 2
    num //= 2
    
    largest = max(largest, 2)

if num != 1:
    #check other primes
    factor = 3
    while num != 1:
        if num % factor == 0:
            #found prime factor
            largest = max(largest, factor)    
            num //= factor
    else:
        factor += 2 # check nest odd number

print(f"{largest} if the largest prime facter for {num_copy}.")
