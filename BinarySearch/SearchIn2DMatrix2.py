# Write an efficient algorithm that searches for a value target
#  in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
def binary_search_in_line(nums, target):
    left = 0 
    right = len(nums) - 1
    while (left <= right):
        middle = left + (right - left) // 2
        if (nums[middle] == target):
            return True
        elif (nums[middle] < target):
            left = middle + 1 
        else:
            right = middle - 1
    return False

def searchMatrix(matrix, target):

    for i in range(len(matrix)):
        if (binary_search_in_line(matrix[i], target)):
            return True

    return False




matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(searchMatrix(matrix, target))