# Given an m x n binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.
from collections import deque
from typing import List:
def maximalSquare(matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) # Get the dimensions of the matrix
        dp = [[0] * (cols + 1) for _ in range(rows + 1)] # Initialize DP table with extra row and column
        max_side_length = 0 # Maximum side length of a square of '1's

        for row in range(rows):
            for col in range(cols):
                # Check if the current element is a '1'
                if matrix[row][col] == '1':
                    # Update the DP table by considering the top, left, and top-left neighbors
                    dp[row + 1][col + 1] = min(
                        dp[row][col + 1],     # Top
                        dp[row + 1][col],     # Left
                        dp[row][col]          # Top-Left
                    ) + 1
                    # Update the max side length found so far
                    max_side_length = max(max_side_length, dp[row + 1][col + 1])
      
        # Return the area of the largest square
        return max_side_length * max_side_length



    

mat =  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


print(maximalSquare(mat))