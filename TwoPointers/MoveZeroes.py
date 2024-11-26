
# Given an integer array nums, move all 0's to the end of 
# it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 
def moveZeroes(nums):

    non_zero = 0 
    for i in range(len(nums)):
        if (nums[i] == 0):
            nuls += 1
        elif (nums[i] != 0):
            nums[non_zero] = nums[i]
            non_zero += 1
    for i in range(non_zero, len(nums),1):
        nums[i] = 0
        