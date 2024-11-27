# Given an array of integers nums sorted in non-decreasing order,
#  find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.
def searchRange(nums, target):
    answer = [-1,-1]

    def binary_search(nums, target, is_binary_search_left):
        left = 0
        right = len(nums) -1 
       
        indx = -1 
        while(left <= right):
            middle = left + (right - left) // 2

            if (nums[middle] == target):
                indx = middle
                if (is_binary_search_left):
                    right = middle - 1
                else:
                    left = middle + 1
            elif (nums[middle] < target):
                left = middle + 1
            elif (nums[middle] > target):
                right = middle - 1 
        return indx


    answer[0] = binary_search(nums, target, True)
    answer[1] = binary_search(nums, target, False)
    return answer

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))