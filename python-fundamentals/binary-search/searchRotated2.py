# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/?envType=daily-question&envId=2023-12-14

    # binary search for the max
    # then divide the interval in two
    # then binary searc for num in both intervals

def findMax(left, right):
    if left == right: 
        return left
    if right - left == 1: 
        if nums[left] > nums[right]:
            return left
        else: return right

    mid = (left + right)//2
    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: return mid

    leftSide = findMax(left, mid - 1)
    rightSide = findMax(mid + 1, right)
    return max(leftSide, rightSide)    

def search(nums):

    return 

nums = [1,2,3,4]