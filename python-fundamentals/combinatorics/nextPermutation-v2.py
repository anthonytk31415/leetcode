
# if i == -1: 
from math import inf

# Time: O(nlogn)
# Space: O(1)

# idea is that the next perm lexicographical order will be where you just make the number "1 unit larger". 
# 

# First, from the right side to the left of nums, find index i where nums[i] < nums[i + 1]. 
# That means the nums from k=i+1 -> are sorted in descending order (they're max).
# You want to make the portion of nums from i onward slightly higher by exchanging 
# nums[i] with a number from k onward where nums[j] is smallest and nums[j] > nums[i], 
# and j is the largest index possible (i.e. when duplicates of nums[j] exist). This is so we can 
# then we reverse the nums k onward so nums is the smallest!


def nextPermutation (nums):
    i = -1
    for x in range(len(nums)-1, 0, -1):
        if nums[x-1]  < nums[x]: 
            i = x - 1
            break
    k = i + 1
    if i > -1: 
        j = None
        for y in range(i+1, len(nums)):
            if nums[y] > nums[i]:
                if not j: 
                    j = y
                else: 
                    if nums[y] <= nums[j]: 
                        j = y
        nums[i], nums[j] = nums[j], nums[i]
    nums[k:] = nums[k:][::-1]
    return

# nums = [3,2,1]
# nums = [1,2,3]
nums = [1,2,4,3] # --> [1,3,2,4]

print(nextPermutation(nums))
print(nums)