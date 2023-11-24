from math import inf 

# This is much easlier than shortest subarray because it doesnt have negatives.
# Approach this with the sliding window. 
# Create right and left pointers. left = 0. iterate across right with a for loop. 
# I used prefixSum for O(1) eval criteria 
# once the sum >= k: try to remove elementes from the left with a while loop. Once you violate the window, exit your loop. 

def minSubArrayLen(target, nums):

    def findCurSum(left, right):
        if left == 0: 
            return prefixSum[right]
        return prefixSum[right] - prefixSum[left - 1] 
    
    prefixSum = [x for x in nums]
    for i in range(1, len(nums)):
        prefixSum[i] = prefixSum[i] + prefixSum[i-1]

    left, minLength = 0, inf
    for right in range(len(prefixSum)):
        curSum = findCurSum(left, right)
        while left <= right and curSum >= target: 
            minLength = min(minLength, right - left + 1)
            left += 1
            curSum = findCurSum(left, right)

    return 0 if minLength == inf else minLength

target = 11
nums = [1,1,1,1,1,1,1,1]

# target = 7
# nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))