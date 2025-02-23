#lesson 12

#input
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

#processing
angle_sum = sum([angle1, angle2, angle3])

if angle_sum != 180:
    print("Error!")
else:
    if angle1 == angle2 == angle3: #chaining operator ==
        print("Equilateral")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3: #as long as one statement of and is true, print scalene
        print("Scalene")
    else:
        print("Isosceles")
