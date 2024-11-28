# Given a string s consisting of words and spaces, return the 
# length of the last word in the string.

# A word is a maximal 
# substring
# Substring
# A substring is a contiguous non-empty sequence of characters within a string.

# consisting of non-space characters only.

def lengthOfLastWord(s):
    lenght = 0
    for i in range (len(s)-1, -1, -1):
        if(s[i] != ' '):
            lenght += 1
        elif (s[i] == ' ' and lenght > 0):
            break

    return lenght 
    

s = 'the;lekj dalksfjl'
print(lengthOfLastWord(s))
