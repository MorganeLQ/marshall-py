#lesson 10

#input
phone = input("Enter the last 4 digits of the phone number: ")

#string index to process individual parts of string
if phone[0] == 8 or phone [0] == 9: #or if phone[0] in {'8', '9'}:
    #string list or tuple, you may access individual items by indexing with square brackets
    # first item is at 0
    if phone[-1] in {'8', '9'}:
    #if last digit (negative indexing goes backwards)
        if phone [1] == phone[2]:
            print(f"The phone number with {phone} as its last four digits is a telemarket.")
        else:
            print(f"The phone number with {phone} as its last four digits is not a telemarket.")
    else:
        print(f"The phone number with {phone} as its last four digits is not a telemarket.")
else:
    print(f"The phone number with {phone} as its last four digits is not a telemarket.")
