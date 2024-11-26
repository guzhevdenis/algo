# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown 
# pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
#  nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target,
#  return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    left = 0 
    right = len(nums) - 1
    previous = nums[0]
    rotation_index = 0
    for i in range (1,len(nums)):
        if (nums[i] < previous):
            rotation_index = i
        previous = nums[i]


    while(left <= right):
        middle = left + (right - left) // 2 

        if (nums[middle] == target):
            return middle
        
        elif(nums[middle] >= nums[left]):
            if nums[left]<= target <= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        else:
            if  nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1

        
    return -1

nums = [5,6,7,0,1,2,4]
#nums = [0,1,2,4,5,6,7]
print(search(nums,3))