#lesson 26

#creating functions
def is_divisible(num1, num2):
    #is num1 divisible by num2

    return num1 % num2 == 0


def factor_count(number):
    #determines the number of factors the argument has

    counter = 0
    for divider in range(1, number+1):
        if is_divisible(number, divider):
            counter += 1
    return counter

upper_limit = int(input("Enter N: "))

for num in range(1, upper_limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors.")
