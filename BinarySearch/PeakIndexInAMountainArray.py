# You are given an integer mountain array arr of length 
# n where the values increase to a peak element 
# and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.
def peakIndexInMountainArray(arr):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        middle = left +(right-left)//2
        if (arr[middle-1] < arr[middle] > arr[middle+1]):
            return middle
        elif (arr[middle-1] < arr[middle+1] > arr[middle]):
            left = middle + 1
        elif (arr[middle+1] < arr[middle-1] > arr[middle]):
            right = middle -1


nums = [0,1,5,3,6,1,2,3]
print(peakIndexInMountainArray(nums))