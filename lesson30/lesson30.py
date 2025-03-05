#lesson 30

def create_line(num):
    text = ''
    for i in range (1, num+1):
        if i % 2 == 0:
            #i is even
            text += '0'
        else:
            #i is odd
            text += '1'
    return text

def output_pattern(num):
    for i in range(1, num+1):
        print(create_line(i))

v = output_pattern(5)
print(v)
