# Given a square matrix mat, 
# return the sum of the matrix diagonals.

# Only include the sum of all
# the elements on the primary diagonal
# and all the elements on the secondary
# diagonal that are not part of the primary diagonal.

from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    n = len(mat)
    result = 0
    for i in range(n):
        result += mat[i][i] + mat[i][n - i - 1]
    if n % 2 == 1:
        result -= mat[n // 2][n // 2]

    return result




mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(diagonalSum(mat))