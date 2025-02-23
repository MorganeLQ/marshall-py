#lesson 13

#input
month = (int(input("Enter month number: ")))
day = (int(input("Enter day number: ")))

#processing 
if month == 2 and day == 18:
    print("special")
else:
    if month < 2:
        print ("Before")
    elif month > 2:
        print("After")
    else:
        #in the month of february
        if day < 18:
            print ("Before")
        else:
            print ("After")
