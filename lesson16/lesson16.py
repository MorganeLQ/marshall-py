#lesson 16

#range(a, b, step) --> range from a to b, not includin b, with "step" based interval

#for loop used to look through values in iterable object
for num in range(1, 51):
    #num --> variable represent individual item in range
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz!")
    elif num % 3 == 0:
        print("Fizz!")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
