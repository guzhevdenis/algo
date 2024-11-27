# Given two strings s and t, return true if t is an 
# anagram
# of s, and false otherwise.
def isAnagram(s, t):
    if (sorted(s) == sorted(t)):
        return True
    return False

s = "anagham"
t = "nagaram"
print(isAnagram(s,t))
