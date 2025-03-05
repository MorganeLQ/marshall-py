#lesson 31

#create function to determine if too strings are anagrams
def is_anagram(word1, word2):
    #if length of words is not equal, not anagram
    if len(word1) != len(word2):
        return False
    else:
        #if characters in words are not identical, not anagram
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
        return True

a = is_anagram(input("Enter first word: "), input("Enter second word: "))
print(a)
