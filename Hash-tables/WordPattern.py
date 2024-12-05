# Given a pattern and a string s, 
# find if s follows the same pattern.

# Here follow means a full match, 
# such that there is a bijection between a letter in pattern 
# and a non-empty word in s. Specifically:

# Each letter in pattern maps to 
# exactly one unique word in s.
# Each unique word in s maps to 
# exactly one letter in pattern.
# No two letters map to the same word, and no
# two words map to the same letter.
 
def wordPattern(pattern, s):

    pattern_dict = {}
    words_dict = {}

    words = s.split()

    if len(pattern) != len(words):
        return False

    for i, (a, b) in enumerate(zip(pattern, words), 1):
        if a in pattern_dict:
            if (pattern_dict[a] != b):
                return False
        if b in words_dict:
            if(words_dict[b] != a):
                return False
        
        pattern_dict[a] = b
        words_dict[b] = a
    return True


pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern,s ))