#lesson 21

#input
upper_limit = int(input("Enter a number: "))

max_count = 0
result_num = 0

total_factors = 0

for num in range(1, upper_limit+1):
    total_factors = 0 # reset variable each iteration
    
    #count number of factors for num
    for divider in range(1, num+1):
        if num % divider ==0:
            total_factors += 1
    
    if total_factors > max_count:
        max_count = total_factors #hold largest count so far
        result_num = num #generate most factors so far
        
print(f"{result_num} had the most factors, with {max_count} factors.")
