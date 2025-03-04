#lesson 27

#create function to remove non alphabetical variables from string
def string_cleaner(text):
    result = '' #initialize empty string
    for character in text:
        #strings are immutable
        if character.isalpha():
            #if character is a member of the ACII table
            result = result + character.lower()
            #returns in lowercase

    return result

value = string_cleaner(input("Enter text to clean: "))
print(value)
