#lesson 11

#input
point = input() 

#split the string from where it can find the given product (a space)
#"10 -11" --> ["10", "-11"]
point = point.split(' ') 

#create an iterable object
#point is ["10", "-11"] -->iterable(10, -11) --> [10, -11]
point = map(int, point)
print (point)

#variable unpacking
x, y = point
print(f"x is {x}")
print(f"y is {y}")

#quadrant selection
if x > 0:
    if y > 0:
        print(f"The point of ({x},{y}) is in Quadrant 1.")
    else:
        print(f"The point of ({x},{y}) is in Quadrant 4.")
else:
    if y > 0:
        print(f"The point of ({x},{y}) is in Quadrant 2.")
    else:
        print(f"The point of ({x},{y}) is in Quadrant 3.")
