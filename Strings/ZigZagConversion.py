# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
# rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    idx, d = 0, 1
    rows = [[] for _ in range(numRows)]
    #idx - индекс ряда 
    for char in s:
        rows[idx].append(char)
        if idx == 0:
            d = 1
        elif idx == numRows - 1:
            d = -1
        idx += d

    for i in range(numRows):
        rows[i] = ''.join(rows[i])

    return ''.join(rows)   

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))