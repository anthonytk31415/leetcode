# from bisect import bisect_left

# You find the left and right most increasing subarrays where left starts at i = 0 and right ends at j = len(nums)
# Two Pointers Time: O(n) implementation with O(1) Space

def incremovableSubarrayCount(nums):

    left, right = 0, len(nums) - 1
    # find largest Left side of nums in increasing
    while left + 1 < len(nums) and nums[left] < nums[left + 1] : 
        left += 1

    # now find the right side of nums increasing 
    while right - 1 >= 0 and nums[right - 1] < nums[right]: 
        right -= 1
    
    # the whole array is increasing 
    if left >= right: 
        n = len(nums)
        return n *(n + 1) // 2

    # add subarrays formed by left and right increasing subarrays
    res = 0
    res += left + 1
    res += len(nums) - right + 1

    # use two pointers to find the smallest gap that can be removed between each i on the left 
    # and j on the right (starting at j=right). You never push j backwards. 
    i, j = 0, right
    for i in range(0, left + 1):
        while j < len(nums) and nums[i] >= nums[j]: j += 1
        if j < len(nums): res += len(nums) - 1 - j + 1
    return res

# arr = [1,2,3,4]
# arr = [1]
# arr2 = [1,2,6, 5,7, 8]
arr = [6,5,7,8] # 7

# print(incremovableSubarrayCount(arr1))
print(incremovableSubarrayCount(arr))