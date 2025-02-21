# Lesson 8
#user input
tournament = input("Tournament wins and loses: ")

#count wins and loses
wins = tournament.count('W')
loses = tournament.count('L')

#sort groups
if (wins > 0)
	for wins in range(5, 7)
    	print("Group 1")
    for wins in range(3, 5)
    	print("Group 2")
    for wins in range(1, 3)
    	print("Group 3")
else
	print("Eliminated")