# You are given an m x n integer matrix matrix with 
# the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than
#  the last integer of the previous row.
# Given an integer target, return true if target 
# is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
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
    left = 0 
    right = len(matrix) - 1
    while (left <= right):
        middle = left + (right - left) // 2
        if (matrix[middle][0]<= target <= matrix[middle][len(matrix[0])-1]):
            return (binary_search_in_line(matrix[middle], target))
                
        elif(target > matrix[middle][len(matrix[0])-1]):
            left = middle + 1 
        else:
            right = middle -1 
    return False




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(searchMatrix(matrix, target))