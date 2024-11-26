# Given a sorted array of distinct integers and 
# a target value, return the index if the target is found. 
# If not, return the index where it would be i
# f it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    middle = 0
    while (left <= right):
        if (left == right):
            if nums[left] >= target:
                return left
            else:
                return left + 1
        middle = left + (right - left)//2
        if (nums[middle] > target):
            right = middle - 1
        elif (nums[middle] < target):
            left = middle + 1
        elif (nums[middle] == target):
            return middle
    return middle
    

nums = [1]
print(searchInsert(nums,1))