#lesson 28

#palindrome checker
def palindrome_checker(text):
    if len(text) < 4:
        # for string with len smaller than 4, is palyndrome
        return text[0] == text[-1]
        #if first and last variable equal, is true
    else:
        # text 4 or greater
        midpoint = len(text) // 2
        #if len is odd, ignore middle character
        for i in range(0, midpoint):
            left = text[i]
            right = text[(-1*i)-1]

            #check that left and right are equal
            if left != right:
                print(f"{text} is not a palindrome")
                return False #auto terminate loop
        print(f"{text} is a palindrome")
        return True

string = palindrome_checker(input("Enter text: "))
