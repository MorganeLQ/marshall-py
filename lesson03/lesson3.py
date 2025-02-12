# Lesson 3
print("Hello, world")

# input
tiles = input("Enter the number of tiles: ")
# input always a string
tiles = int(tiles)
#converting a value to integer

#Square root is exponent of a half
calculation = int((tiles **0.5) // 1)
# int to turn back into integer (whole numer)

# or...
# import math
# calculations = math.sqrt(tiles)

print(f"calculation is {calculation}") 
# f: to print right value inside curly brace (without will print "calculation")


print(f"Number of tiles: {tiles}") 
