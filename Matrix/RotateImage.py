# You are given an n x n 2D matrix representing an image, 
# rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, 
# which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    edge_length = len(matrix)

    top = 0
    bottom = edge_length - 1


#Flipping upside down
    while top < bottom:
        for col in range(edge_length):
            temp = matrix[top][col]
            matrix[top][col] = matrix[bottom][col]
            matrix[bottom][col] = temp
        top += 1
        bottom -= 1

#Flipping across main diagonal
    for row in range(edge_length):
        for col in range(row+1, edge_length):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
    
    return matrix
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotate(matrix)

print(matrix)