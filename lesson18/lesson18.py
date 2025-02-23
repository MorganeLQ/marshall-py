#lesson 18

#input
num = int(input("Enter an integer to find factors: "))

divider = 1
while divider <=  num:
    print(f"Divider is: {divider}.")
    
    if num % divider == 0:
        # if == 0, it is factor, perfectly divisible
        print(f"{divider} is a factor for {num}.")
    else:
        print(f"{divider} is not a factor for {num}.")
    
    divider +=1 #sets new value for divider
