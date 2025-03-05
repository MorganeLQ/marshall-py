#lesson 29

#create function
#analyze string, return # of consonants

def num_consonant(text, vowel=False):

    i = 0
    #check each variable in text
    for character in text:
        character = character.lower() #lowercase all characters
        #if character is alphabetical
        #and not a character from list, count it
        if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
                i += 1
    #return # of consonants
    return i
    
    if not vowel:
        return i
    else:
        i = 0
        #check each variable in text
        for character in text:
            character = character.lower() #lowercase all characters
            #if character is alphabetical
            #and not a character from list, count it
            if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
                i += 1
        #return # of consonants
        return i
        
a = num_consonant(input("Enter text to count consonants: "))
print(f"There are {a} consonents in the text.")
