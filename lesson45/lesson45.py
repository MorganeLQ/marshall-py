# Lesson 45
def word_length(a_list):
    return {key : len(key) for key in a_list}

print(word_length(["banana", "fig", "strawberry"]))

def d_fib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] =result[i-1] + result[i-2]
        return result

print(d_fib(10))