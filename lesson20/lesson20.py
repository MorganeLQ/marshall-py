#lesson 20

total_sum = 0

for num in range(1, 10000):
    # if num is perfect number
    
    factor_sum = 0 #resets to 0 at every iteration
    for divider in range(1, num):
        if num % divider == 0:
            # divider is factor, add to factor_sum
            factor_sum += divider
    # end for loop
    if factor_sum == num:
        #perfect number
        total_sum += num
        print(f"{num} is a perfect number.")
print(f"The total sum of all perfect numbers under 10 000 is {total_sum}.")
