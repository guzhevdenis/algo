# Hoare’s Partition Scheme works by initializing two indexes that
# start at two ends, the two indexes move toward each other until
# an inversion is (A smaller value on the left side and greater value on
#  the right side) found. When an inversion is found, two values are swapped
# and the process is repeated.

def partition(arr, low, high):

    pivot = arr[low]
    i = low - 1
    j = high + 1

    while (True):

        # Find leftmost element greater than
        # or equal to pivot
        i += 1
        while (arr[i] < pivot):
            i += 1

        # Find rightmost element smaller than
        # or equal to pivot
        j -= 1
        while (arr[j] > pivot):
            j -= 1

        # If two pointers met.
        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]
    
    
def quickSort(arr, low, high):
    ''' pi is partitioning index, arr[p] is now 
    at right place '''
    if (low < high):

        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)


''' Function to print an array '''


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)








