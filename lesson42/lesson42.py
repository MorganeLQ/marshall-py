# Lesson 42
def possible_sum(a_list, target):
    for i, value in enumerate(a_list):
        new_target = target - value
        if new_target in a_list[i+1:]:
            return True
            
    return False

test = [1, 5, 3, 6, 5, 88, 0]
target = 3

print(f"Can {target} be made from two unique values in: {test}?")
print(possible_sum(test, target))