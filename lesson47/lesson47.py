# Lesson 47
def r_sum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + r_sum(num-1)

print(f"Sum of all numbers from 1 to 10: {r_sum(10)}")