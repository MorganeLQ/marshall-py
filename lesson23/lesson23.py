#lesson 23

#create infinite loop
loop = True

#initialize variables
total_sum = 0
counter = 0

while loop:
    
    user_input = input("Enter the mark OR \"Exit\" to stop inputting marks: ")
    
    if user_input.lower().capitalize() == "Exit":
        loop = False #exit programe
        break # exit loop
    else:
        mark = int(user_input)
        if 0 <= mark <= 100: #valid input
            total_sum += mark
            counter += 1
        else:
            print("Invalid input")

average = total_sum / counter
            
print(f"Your average is: {average}")
