from math import inf 
from functools import lru_cache

# This is a sliding window problem. The key is knowing the width and introducing a third pointer: a mid.
# when you have a valid window (you've counted at least k max's), you move mid to the last of the k max's 
# where the current pointer is at the first k. then the subarrays added  = mid - left + 1. 
# We define left here, but left really never changes. 

# Extra credit: what if this was the max element of the subarray 

def countSubarrays(nums, k):

    curCount = 0
    maxNums = max(nums)
    left = 0
    mid = -1
    res = 0
    midCount = 0
    for i, right in enumerate(nums):
        if right == maxNums: 
            curCount += 1

        if curCount >= k: 
            #move left to the first value < curMax; left never changes
            # while nums[left] > maxNums: 
            #     left += 1
            #move mid to the kth curMax
            while midCount < curCount - k + 1:
                mid += 1
                if nums[mid] == maxNums:
                    midCount += 1
        res += mid - left + 1

    return res


# nums = [1,3,2,3,3]
# k = 2
# nums = [1,2,4,4,1,2,1,2,4]
# k = 2

# nums = [37,20,38,66,34,38,9,41,1,14,25,63,8,12,66,66,60,12,35,27,16,38,12,66,38,36,59,54,66,54,66,48,59,66,34,11,50,66,42,51,53,66,31,24,66,44,66,1,66,66,29,54]
# k = 5

nums = [28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49]
k = 1

print(countSubarrays(nums, k))