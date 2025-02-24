#lesson 24

#initialize variables

name = '' # empty string for loop

longest_length = 0
longest_name = ''

while name != 'X':
    #user input
    name = input("Enter your name or 'X' to exit:")
    
    if name != 'X':

        current_length = len(name)
    
        if current_length > longest_length:
            longest_length = current_length
            longest_name = name
    else:
        print("End of the inputs.")

if longest_name:
    print(f"The longest name with {longest_length} characters is {longest_name}")
else:
    print("Not enough data")
