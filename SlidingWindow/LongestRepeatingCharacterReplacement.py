# You are given a string s and an integer k. 
# You can choose any character of the string 
# and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing 
# the same letter you can get after performing the above operations.

def characterReplacement(s: str, k: int) -> int:

    if (len(s) == 0):
        return 0

    last_value = [-1] * 256
    maxLenght = 0

    left = s[0]
    right = s[0]
    start = 0
    end = 0

    for i in range(len(s)):
        if last_value[ord(s[i])] != -1:
            right = s[0]
            left = s[0]
        

        last_value[ord(s[i])] = i

        maxLenght = max(maxLenght, end - start + 1)
 


    return 0


s = "AABABBA"
k = 1

characterReplacement(s, k)
print(s)