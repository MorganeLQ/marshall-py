# Lesson 32

def duplicates(word1, word2):
    
	if not word1 or not word2:
    	return [] #empty list if no input
	else:
    	set_word1 = set(word1)
        set_word2 = set(word2) #create a set without duplicates of individual chracters in word2
    	#membership operator is more efficient with sets
        
    	result = [] #empty list to add duplicates 
    	for character in word1:
        	if character in set_word2:
            	result.append(character)
            
		return sorted(result)

list = (input("Enter word 1: "), input("Enter word 2: "))
print(duplicates((f{list}))