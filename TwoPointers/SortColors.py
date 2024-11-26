# Given an array nums with n objects colored red, 
# white, or blue, sort them in-place so that objects of the same color are adjacent,
#  with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, 
# white, and blue, respectively.

# You must solve this problem without using the library's sort function.
def sortColors(nums):

    red = 0
    white = 0 
    blue =0 

    for element in nums:
        if (element == 0):
            red += 1
        elif (element == 1):
            white += 1
        elif (element == 2):
            blue += 1

    for i in range(red):
        nums[i] = 0
    for i in range(red,red+white,1):
        nums[i] = 1
    for i in range(red+white,red+white+blue):
        nums[i] = 2