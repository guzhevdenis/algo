# Given a string s, find the length of the longest 
# substring
# without repeating characters.

def longestUniqueSubstr(s):
    n = len(s)
    
    res = 0

    # last index of all characters is initialized as -1
    last_index = [-1] * 256

    # Initialize start of current window
    start = 0

    # Move end of current window
    for end in range(n):
        
        # Find the last index of s[end]
        # Update starting index of current window as
        # maximum of current value of start and last index + 1
        start = max(start, last_index[ord(s[end])] + 1)

        # Update result if we get a larger window
        res = max(res, end - start + 1)

        # Update last index of s[end]
        last_index[ord(s[end])] = end

    return res

s = "geeksforgeeks"


