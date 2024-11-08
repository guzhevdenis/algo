#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#You can return the answer in any order.
def twoSum(nums, target):
    hash_m = {}
    for i, element in enumerate(nums):
        if (target - element) in hash_m: 
            return [i, hash_m[target-element]]
        hash_m[element] = i


nums = [3,2,4]
target = 6
answer = twoSum(nums, target)
print(answer)

#We use hash table because it is searched faster 