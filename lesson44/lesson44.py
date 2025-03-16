# Lesson 44
def c_frequency(word):
    clean_word = sorted(word.lower())
    
    answer = {}
    
    for character in clean_word:
        if character not in answer:
            answer[character] = 1
        else:
            answer[character] += 1
    return answer

result = c_frequency("Hello")
print(f"Characyer Frequency of hello:\n{result}")