def threeSum(nums,target):
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                secondNum  = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                if potentialSum > target:
                    k -= 1
                elif potentialSum < target:
                    j += 1
                else:
                    triplets.add((firstNum , secondNum ,thirdNum))
                    j += 1
                    k -= 1
        return triplets

def FourSum(nums, target):
    nums.sort()
    
    quadroplets = set()
    for i in range(len(nums) - 3):
        firstNum = nums[i]
        triplets = threeSum(nums[(i+1):], target-firstNum)
        if triplets:
             for triplet in triplets:
                a,b,c = triplet
                quadroplets.add((firstNum,a,b,c))
    return    quadroplets

nums = [1,0,-1,0,-2,2]
target = 0
print(FourSum(nums,target))

