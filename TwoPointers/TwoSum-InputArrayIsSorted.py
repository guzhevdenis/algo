#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
#Return the indices of the two numbers, index1 and index2, 
# added by one as an integer array [index1, index2] of length 2.
#
#The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
#
#Your solution must use only constant extra space.

def twoSum(numbers, target):
        i = 0
        j = len(numbers)-1
        
        sum = -1*target
        
        while(i<len(numbers) and j > 0):
            sum = numbers[i] + numbers[j]
            if (sum > target):
                j = j - 1
            elif(sum < target):
                i = i + 1 
            elif(sum == target):
                return [i+1,j+1]
        return []

numbers = [1,2,3,5]
target = 4

print(twoSum(numbers, target))

#We just use the idea of two pointers
#check git