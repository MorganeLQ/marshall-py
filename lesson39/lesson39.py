# Lesson 39

def gcd(num1, num2):
    for divider in range(min(num1,num2), 0, -1):
        if num1 % divider == 0 and num2 % divider == 0:
            return divider
    return 1

first = print("Enter first number: ")
second = print("Enter second number: ")

print(f"The GCD of {first} and {second}: {gcd(first, second)}")