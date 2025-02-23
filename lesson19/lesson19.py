#lesson 19

#input
num = int(input("Enter a number to find if it is a prime number: "))

is_prime = True #assumes all number is prime until proven otherwise

for divider in range(2, num):
    if num % divider == 0:
        #if divider is a factor, num is not prime
        is_prime = False
        break #keyword allows exit from for loop

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")
