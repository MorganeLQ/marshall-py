# Lesson 34

def csv_to_list(test):
    csv = text.split(',') #split text at coma
    a_list = [] #create empty list to put split text
    
    for item in csv:
        a_list.append(int(item))
    
    return a_list

def rand_list(start, end, frequent):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            new_value = randrange(start, end+1)
            a_list.append(new_value)
        return a_list
    else:
        return []
        
print(csv_to_list("1,2,3,4,5"))
print(rand_list(1,1000,30))