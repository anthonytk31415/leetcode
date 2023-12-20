from collections import Counter
from math import inf 

# Sliding window! Time: O(n), Space: O(1)

def maximumSubarraySum(nums, k):
    countNums = Counter(nums[:k-1])
    curSum = sum(nums[:k - 1])
    maxSum = 0
    for i in range(k-1, len(nums)):
        countNums[nums[i]] += 1
        curSum += nums[i]
        if len(countNums) == k: maxSum = max(maxSum, curSum)
        curSum -= nums[i - k + 1]
        countNums[nums[i - k + 1]] -=1
        if countNums[nums[i - k + 1]] == 0: del countNums[nums[i - k + 1]] 
    return maxSum 

nums = [1,5,4,2,9,9,9]
k = 3

# nums = [4,4,4]
# k = 3

print(maximumSubarraySum(nums, k))