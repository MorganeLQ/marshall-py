#lesson 9

#import statement
from random import choice

#set up loop for user input, while invalid (no user input) continue
invalid = True
player = '' #initialize variable

while invalid:
    #ask for user input
    player = input("Enter rock, paper, or scissors: ")
    
    #create a set of possible values
    #often use operator in python with sets (faster executaion)
    if player in {'rock', 'paper', 'scissors'}:
        #if player enters a valid input, while loop ends
        invalid = False
#end of while loop

#processing
cpu = choice(['rock', 'paper', 'scissors'])
print(f"The CPU chose {cpu}.")

#game logic
if player == cpu:
    print("Tie Game!")
else:
    #Garanteed win
    if player == 'rock':
        if cpu == 'paper':
            print("The CPU has won the game!")
        else:
            print("The player has won the game!")
    elif player == 'paper':
        if cpu == 'scissors':
            print("The CPU has won the game!")
        else:
            print("The player has won the game!")
    else:
        #player chose scissors
        if cpu == 'rock':
            print("The CPU has won the game!")
        else:
            print("The player has won the game!")
