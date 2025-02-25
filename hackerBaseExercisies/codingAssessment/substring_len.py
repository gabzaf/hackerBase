##write a function that takes a string as input and returns the length of the longest substring that contains only two distinct characters.
##For example, given the input string "abcbbbbcccbdddadacb", the function returns 10, because the longest substring that contains only two 
##distinct characters is "bcbbbbcccb"

def solution(s):
    if not s:
        return 0
    
    char_count = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        while len(char_count) > 2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

input_string = "abcbbbbcccbdddadacb"
result = solution(input_string)
print(result)