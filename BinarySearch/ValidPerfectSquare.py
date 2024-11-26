# Given a positive integer num, return true 
# if num is a perfect square or false otherwise.

# A perfect square is an integer that is 
# the square of an integer. In other words, it is the 
# product of some integer with itself.

# You must not use any built-in library function, such as sqrt.
def isPerfectSquare(num):
    left = 1 
    right = num // 2
    if num == 1:
        return True
    while (left <= right):
        middle = (left + (right - left)) // 2
        if (middle * middle == num):
            return True
        elif (middle * middle < num ):
            left = middle + 1
        elif (middle * middle > num):
            right = middle - 1
    return False
print(isPerfectSquare(16))